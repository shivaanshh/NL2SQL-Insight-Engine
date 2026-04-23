# app.py — Smart ChatGPT-like SQL Assistant
import streamlit as st
from chat_engine import chat_with_gpt
from gpt_sql import get_sql_from_prompt
from sql_executor import run_query
from chart_generator import generate_chart
from utils import get_schema_summary
import os
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="🧠 RBC SQL Chat Assistant", layout="wide")
st.title("🧠 RBC Bond Trader AI Assistant")

# Session state
if "chat_logs" not in st.session_state:
    st.session_state.chat_logs = {}
if "active_chat_id" not in st.session_state:
    st.session_state.active_chat_id = None
if "db_uri" not in st.session_state:
    st.session_state.db_uri = None
if "schema_summary" not in st.session_state:
    st.session_state.schema_summary = ""

# Sidebar chat sessions
st.sidebar.header("💬 Chat Sessions")
if st.sidebar.button("➕ New Chat"):
    new_id = datetime.now().strftime("Chat_%Y-%m-%d_%H:%M:%S")
    st.session_state.chat_logs[new_id] = []
    st.session_state.active_chat_id = new_id

for cid in st.session_state.chat_logs:
    if st.sidebar.button(str(cid), key=str(cid)):
        st.session_state.active_chat_id = cid

if not st.session_state.active_chat_id and st.session_state.chat_logs:
    st.session_state.active_chat_id = list(st.session_state.chat_logs.keys())[0]

chat = st.session_state.chat_logs.setdefault(st.session_state.active_chat_id, [])

# Sidebar DB connect
st.sidebar.subheader("🗂️ Database Setup")
mode = st.sidebar.radio("Connection type:", ["Upload SQLite File", "Enter DB URI"])

if mode == "Upload SQLite File":
    db_file = st.sidebar.file_uploader("Upload .db file", type=["db"])
    if db_file:
        db_path = f"temp_{db_file.name}"
        with open(db_path, "wb") as f:
            f.write(db_file.read())
        st.session_state.db_uri = f"sqlite:///{db_path}"

if mode == "Enter DB URI":
    uri_input = st.sidebar.text_input("Paste DB URI")
    if uri_input:
        st.session_state.db_uri = uri_input

if st.session_state.db_uri:
    db_uri = st.session_state.db_uri
    dialect = db_uri.split(":")[0]

    if not st.session_state.schema_summary:
        try:
            schema = get_schema_summary(db_uri)
            st.session_state.schema_summary = schema
        except Exception as e:
            st.error(f"❌ Schema load failed: {e}")
            st.stop()

    with st.sidebar.expander("📋 DB Schema"):
        st.code(st.session_state.schema_summary)

    user_input = st.chat_input("Ask anything or query your database...")
    last_df = None

    if user_input:
        chat.append(("user", user_input))
        try:
            explanation = chat_with_gpt(user_input, st.session_state.schema_summary)
            # Detect intent: is this query-related?
            keywords = ["select", "table", "plot", "rate", "chart", "bar", "line", "graph", "between", "from", "where"]
            is_data_query = any(w in user_input.lower() for w in keywords)

            # Fallback: "show table prime_rate"
            fallback_sql = None
            if "show" in user_input.lower() and "table" in user_input.lower():
                words = user_input.lower().split()
                for i, word in enumerate(words):
                    if word == "table" and i + 1 < len(words):
                        fallback_sql = f"SELECT * FROM {words[i+1]}"
                        break

            if is_data_query or fallback_sql:
                sql = fallback_sql if fallback_sql else get_sql_from_prompt(user_input, st.session_state.schema_summary, dialect)
                chat.append(("sql", sql))
                if sql.strip().lower().startswith("select"):
                    df = run_query(db_uri, sql)
                    chat.append(("result", df))
                else:
                    chat.append(("error", "❌ Not a SELECT query."))
            else:
                chat.append(("assistant", explanation))

        except Exception as e:
            chat.append(("error", f"❌ {str(e)}"))

    # Render chat
    for i, (role, msg) in enumerate(chat):
        with st.chat_message("user" if role == "user" else "assistant"):
            if role == "sql":
                st.code(msg, language="sql")
            elif role == "result":
                st.dataframe(msg)
                last_df = msg
                st.download_button("⬇ Download CSV", msg.to_csv(index=False), "results.csv", mime="text/csv", key=f"download_{i}")
            elif role == "error":
                st.error(msg)
            else:
                st.markdown(msg)

    # Chart options
    if last_df is not None:
        with st.expander("📊 Visualize this result"):
            x_axis = st.selectbox("X-axis", last_df.columns)
            y_axis = st.selectbox("Y-axis", last_df.columns)
            chart_type = st.radio("Chart Type", ["Bar", "Line", "Scatter", "Histogram", "Pie", "Area", "Bubble", "Heatmap"])
            if st.button("Generate Chart"):
                st.subheader(f"{chart_type} Chart: {y_axis} vs {x_axis}")
                generate_chart(last_df, x=x_axis, y=y_axis, chart_type=chart_type)

else:
    st.info("📂 Upload a database or enter a connection URI to begin.")

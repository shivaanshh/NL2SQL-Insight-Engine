import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pandas as pd
import numpy as np

def generate_chart(df, x=None, y=None, chart_type="Bar"):
    if df is None or df.empty:
        st.warning("⚠️ No data available to plot.")
        return

    try:
        fig, ax = plt.subplots(figsize=(8, 5))

        if chart_type == "Bar":
            ax.bar(df[x], df[y])
        elif chart_type == "Line":
            ax.plot(df[x], df[y], marker='o')
        elif chart_type == "Scatter":
            ax.scatter(df[x], df[y])
        elif chart_type == "Area":
            df_sorted = df.sort_values(x)
            ax.fill_between(df_sorted[x], df_sorted[y])
        elif chart_type == "Histogram":
            ax.hist(df[y], bins=10)
        elif chart_type == "Bubble":
            size_col = st.selectbox("Select bubble size column", df.columns, index=df.columns.get_loc(y))
            ax.scatter(df[x], df[y], s=df[size_col]*10, alpha=0.5)
        elif chart_type == "Pie":
            if x and y:
                pie_df = df.groupby(x)[y].sum()
                ax.pie(pie_df.values, labels=pie_df.index, autopct="%1.1f%%", startangle=90)
                ax.axis('equal')
        elif chart_type == "Heatmap":
            corr = df.corr(numeric_only=True)
            sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)

        if chart_type not in ["Pie", "Heatmap"]:
            ax.set_xlabel(x)
            ax.set_ylabel(y)
            ax.set_title(f"{chart_type} Chart: {y} vs {x}")
            ax.tick_params(axis='x', rotation=45)

        st.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Chart error: {e}")

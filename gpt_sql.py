# gpt_sql.py
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_sql_from_prompt(prompt, schema_summary, dialect="sqlite"):
    system = f"""
You are an expert SQL developer. The user is working with a {dialect.upper()} database.
Schema:
{schema_summary}

Your job is to translate user questions into clean and executable SQL SELECT statements.
- If the user says things like "show the table", generate "SELECT * FROM <table_name>"
- Never include explanations or extra text, just return the valid SQL code.
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

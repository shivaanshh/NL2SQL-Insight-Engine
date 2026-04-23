# chat_engine.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_gpt(prompt, schema_summary):
    system_prompt = f"You are a data analyst expert. The database schema is:\n{schema_summary}\n\nAnswer user questions clearly and concisely."
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

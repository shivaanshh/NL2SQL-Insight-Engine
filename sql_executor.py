# sql_executor.py
import pandas as pd
from sqlalchemy import create_engine

def run_query(db_uri, query):
    engine = create_engine(db_uri)
    with engine.connect() as conn:
        return pd.read_sql(query, conn)

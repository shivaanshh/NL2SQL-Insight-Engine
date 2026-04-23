# utils.py
from sqlalchemy import create_engine, inspect

def get_schema_summary(db_uri):
    engine = create_engine(db_uri)
    insp = inspect(engine)
    summary = ""
    for table_name in insp.get_table_names():
        summary += f"\nTable: {table_name}\n"
        for col in insp.get_columns(table_name):
            summary += f" - {col['name']} ({col['type']})\n"
    return summary

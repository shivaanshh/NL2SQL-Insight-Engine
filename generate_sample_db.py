# generate_sample_db.py
import sqlite3

# Connect and create
conn = sqlite3.connect("sample_bond_data.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE bond_data (
    bond_id TEXT,
    year INTEGER,
    rate REAL,
    yield REAL,
    category TEXT,
    volume_mil REAL
)
""")

# Insert rows
rows = [
    ("BND001", 2020, 2.5, 3.2, "Government", 150.0),
    ("BND002", 2021, 2.7, 3.4, "Corporate", 180.5),
    ("BND003", 2022, 3.0, 3.6, "Government", 160.0),
    ("BND004", 2023, 2.9, 3.5, "Municipal", 170.2),
    ("BND005", 2024, 3.1, 3.8, "Corporate", 200.0),
]

cursor.executemany("INSERT INTO bond_data VALUES (?, ?, ?, ?, ?, ?)", rows)
conn.commit()
conn.close()
print("✅ sample_bond_data.db created!")

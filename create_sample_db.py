import sqlite3

conn = sqlite3.connect("sample.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS prime_rate (
    year INTEGER PRIMARY KEY,
    rate FLOAT
);
""")

data = [
    (2015, 2.5), (2016, 2.7), (2017, 3.0), (2018, 3.5),
    (2019, 3.8), (2020, 2.9), (2021, 2.5),
    (2022, 3.9), (2023, 4.5), (2024, 6.2), (2025, 7.0)
]

cursor.executemany("INSERT OR REPLACE INTO prime_rate (year, rate) VALUES (?, ?);", data)

conn.commit()
conn.close()
print("✅ sample.db created.")

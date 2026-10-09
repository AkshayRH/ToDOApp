import sqlite3

conn = sqlite3.connect("tasks.db")
print("Table Ready")

command = """
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    status TEXT NOT NULL
)
"""
conn.execute(command)

conn.commit()
conn.close()

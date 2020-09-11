import sqlite3

conn = sqlite3.connect("new.db")
cursor = conn.cursor()

try:
    cursor.execute("INSERT INTO populations('New York City', 'NY', 8400000)")
    cursor.execute("INSERT INTO populations('San Fransisco', 'CA', 800000)")
    conn.commit()

except sqlite3.OperationalError:
    print("Ups, ada yang salah. Coba lagi...")

conn.close()

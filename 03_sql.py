import sqlite3

with sqlite3.connect("new.db") as terhubung:
    c = terhubung.cursor()

    perkotaan = [
                ('Boston', 'MA', 600000),
                ('Chicago', 'IL', 2700000),
                ('Houston', 'TX', 2100000),
                ('Phoenix', 'AZ', 1500000)
                ]

    c.executemany('INSERT INTO population VALUES(?, ?, ?)', perkotaan)

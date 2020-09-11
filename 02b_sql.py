import sqlite3

with sqlite3.connect("new.db") as koneksi:
    c = koneksi.cursor()
    c.execute("INSERT INTO population VALUES('Tangerang Selatan', \
        'BT', 750000)")
    c.execute("INSERT INTO population VALUES('Bandung', \
        'JB', 2100000)")

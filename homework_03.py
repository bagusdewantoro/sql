import sqlite3

with sqlite3.connect("cars.db") as koneksi:
    c = koneksi.cursor()

    c.execute("UPDATE inventory SET Quantity = 150000 WHERE Make = 'Honda'")
    c.execute("UPDATE inventory SET Quantity = 200000 WHERE Make = 'Ford'")

    c.execute("SELECT * FROM inventory")
    rows = c.fetchall()
    for r in rows:
        print(r[0], r[1], r[2])

    print("=====================================\n\n")

    c.execute("SELECT quantity FROM inventory WHERE Make = 'Honda'")
    rows = c.fetchall()
    for r in rows:
        print(r[0])

    print("=====================================\n\n")

    c.execute("SELECT * FROM inventory WHERE Make = 'Honda'")
    rows = c.fetchall()
    for r in rows:
        print(r[0], r[1], r[2])

import sqlite3

with sqlite3.connect("new.db") as koneksi:
    c = koneksi.cursor()

    #  c.execute("""CREATE TABLE regions(city TEXT, region TEXT)""")

    kota = [
                ('New York City', 'Northeast'),
                ('San Francisco', 'West'),
                ('Chicago', 'Midwest'),
                ('Houston', 'South'),
                ('Phoenix', 'West'),
                ('Boston', 'Northeast'),
                ('Los Angeles', 'West'),
                ('Houston', 'South'),
                ('Philadelphia', 'Northeast'),
                ('San Antonio', 'South'),
                ('San Diego', 'West'),
                ('Dallas', 'South'),
                ('San Jose', 'West'),
                ('Jacksonville', 'South'),
                ('Indianapolis', 'Midwest'),
                ('Austin', 'South'),
                ('Detroit', 'Midwest')
            ]
    c.executemany("INSERT INTO regions VALUES(?, ?)", kota)
    c.execute("SELECT * FROM regions ORDER BY region ASC")

    barisPrint = c.fetchall()
    for r in barisPrint:
        print(r[0], r[1])

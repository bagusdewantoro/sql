import sqlite3

with sqlite3.connect("cars.db") as terhubung:
    c = terhubung.cursor()
    mobil = [
            ('Ford', 'Ranger', 1000),
            ('Ford', 'Fiesta', 1500),
            ('Honda', 'Jazz', 3000),
            ('Honda', 'Brio', 700),
            ('Honda', 'City', 4500)
            ]

    c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', mobil)

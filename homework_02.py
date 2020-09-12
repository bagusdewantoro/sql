import sqlite3

with sqlite3.connect("cars.db") as terhubung:
    c = terhubung.cursor()
    mobil = [
            ('Ford', 'Ranger', 2004),
            ('Ford', 'Fiesta', 2010),
            ('Honda', 'Jazz', 2005),
            ('Honda', 'Brio', 2015),
            ('Honda', 'City', 2012)
            ]

    c.executemany('INSERT INTO inventory VALUES(?, ?, ?)', mobil)

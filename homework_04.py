import sqlite3

with sqlite3.connect("cars.db") as koneksi:
    c = koneksi.cursor()

    c.execute("""CREATE TABLE orders
                    (Make TEXT, Model TEXT, Order_Date DATE)""")

    tanggal = [
                ('Ford', 'Ranger', '2015-01-05'),
                ('Ford', 'Ranger', '2015-02-10'),
                ('Ford', 'Ranger', '2015-04-20'),
                ('Ford', 'Fiesta', '2016-01-05'),
                ('Ford', 'Fiesta', '2016-03-11'),
                ('Ford', 'Fiesta', '2016-05-05'),
                ('Honda', 'Jazz', '2017-02-05'),
                ('Honda', 'Jazz', '2017-04-05'),
                ('Honda', 'Jazz', '2017-06-05'),
                ('Honda', 'Brio', '2018-03-05'),
                ('Honda', 'Brio', '2018-06-05'),
                ('Honda', 'Brio', '2018-09-05'),
                ('Honda', 'City', '2019-10-05'),
                ('Honda', 'City', '2019-04-05'),
                ('Honda', 'City', '2019-03-05')
            ]

    c.executemany("INSERT INTO orders VALUES(?, ?, ?)", tanggal)
    c.execute("SELECT * FROM orders ORDER BY order_date ASC")

    rows = c.fetchall()
    for r in rows:
        print(r[0], r[1], r[2])

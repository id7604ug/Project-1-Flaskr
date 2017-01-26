import sqlite3
conn = sqlite3.connect('example.db')

c1 = conn.cursor()
c1.execute("SELECT * FROM person")
table1 = c1.fetchall()
for row in table1:
    print(row)

c2 = conn.cursor()
c2.execute('SELECT * FROM address')
table2 = c2.fetchall()
for row in table2:
    print(row)
conn.close()

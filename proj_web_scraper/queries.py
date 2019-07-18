import sqlite3


example1 = """SELECT shape, COUNT(*) FROM ufo_sights group by shape;"""
example2 = """SELECT location, Count(*) as count FROM ufo_sights GROUP BY location ORDER BY count DESC;"""


conn = sqlite3.connect("ufo-db.sqlite")
cursor = conn.cursor()
cursor.execute(example1)

rows = cursor.fetchall()

for row in rows:
    print(row)

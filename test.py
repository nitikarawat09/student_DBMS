import sqlite3
conn = sqlite3.connect("rec.db")
cursor = conn.cursor()
cursor.execute("select * from users ")
r = cursor.fetchall()
print(r)
cursor.close()
conn.close()

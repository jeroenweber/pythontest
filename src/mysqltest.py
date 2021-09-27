import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='jeroen', passwd='weber', database='test')
mycursor = mydb.cursor()
sql = 'INSERT INTO lecturer (id, email, name) VALUES (%s, %s, %s);'
val = (6, 'jeroen.weber@hu.nl', 'jeroen')
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

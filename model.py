import MySQLdb
import peewee

db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="",
                     db="refresh") 

cur = db.cursor()

cur.execute("SELECT orgid, company, status, dt FROM refresh.refresh")

for row in cur.fetchall():
    print row[0]
    print row[1]
    print row[2]
    print row[3]

db.close()
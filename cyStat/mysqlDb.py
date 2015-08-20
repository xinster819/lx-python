import MySQLdb
import DateUtils
print DateUtils.DateUtils.yesterday()
db = MySQLdb.connect(host="10.10.85.62", # your host, usually localhost
                     user="cmt", # your username
                      passwd="cmt", # your password
                      db="cyanstat",
                      port=3306) # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT date FROM labs_stat")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row

import MySQLdb

db = MySQLdb.connect(host="127.0.0.1", # your host, usually localhost
                     user="root", # your username
                      passwd="12345", # your password
                      db="advert",
                      port=3306) # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM agency_daily_record")

# print all the first cell of all the rows
for row in cur.fetchall() :
    print row
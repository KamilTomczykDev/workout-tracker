import mysql.connector

conn_obj = mysql.connector.connect(host="localhost", user="root", passwd="0321")

print(conn_obj)

cur_obj = conn_obj.cursor()

try:
    dbms = cur_obj.execute("show databases")
except:
    conn_obj.rollback()

for x in cur_obj:
    print(x)

conn_obj.close()

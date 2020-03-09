## pip install mysql-connector-python

import mysql.connector

## To establish a connection
# mydb=mysql.connector.connect(host="localhost",user="root",passwd="Feb@2020",auth_plugin='mysql_native_password',)
#
# mycursor=mydb.cursor()
# mycursor.execute("show databases")
#
# for i in mycursor:
#     print(i)

mydb=mysql.connector.connect(host="localhost",user="root",passwd="Feb@2020",auth_plugin="mysql_native_password",database="test1")

mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("show tables")

for i in mycursor:
    print(i)

##use the statement "INT AUTO_INCREMENT PRIMARY KEY"
# which will insert a unique number for each record. Starting at 1, and increased by one for each record
#mycursor.execute("Alter table customers Add column id Int Auto_increment primary key")

myfetch=mycursor.execute("select * from customers")
myfetch=mycursor.fetchall()

for x in myfetch:
    print(x)
    #print(x[3])


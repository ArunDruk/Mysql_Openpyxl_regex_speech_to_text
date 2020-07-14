# pip install mysql-connector
# pip install mysql-connector-python
# pip install mysql-connector-python-rf

import mysql.connector
import pandas as pd
import csv

mydb=mysql.connector.connect(
    user="root",
    passwd="Feb@2020",
    host="localhost",  # This is going to be some URL, if you are connecting to some CLoud where the database resides
    database="db_03_jul_2020"
)

mycursor=mydb.cursor()
################################################## Reading the table 'Country' from database 'World" and writing to excel ##################################################
# mycursor.execute("select name from country")
# mycursor.execute("select * from country")
#
# with open("city_names.csv",'w',newline="",encoding='utf-8') as fw:
#     thewriter=csv.writer(fw)
#     thewriter.writerow(["city_names"])
#     for record in mycursor:
#         thewriter.writerow(record)

######################################################################################################################################################
# mycursor.execute("select continent from country where continent='north america'")
# for record in mycursor:
#     print(record)
#######################################################################################################################################
# mycursor.execute("create database DB_03_Jul_2020")
# mycursor.execute("show databases")
# for record in mycursor:
#     print(record[0])
# mycursor.execute("create table users (name varchar(100), email varchar(100), age integer(3), user_ID integer auto_increment primary key)")
# mycursor.execute("show tables")
# for table in mycursor:
#     print(table[0])

# sql_add_users="Insert into users (name,email,age) values(%s,%s,%s)"
# entry_1=("Arun","arundruk@gmail.com",23)
# mycursor.execute(sql_add_users,entry_1)



# mycursor.execute("select * from users")

# df=pd.read_sql_query("select * from users",mydb)
# print(df)

# pd.read_sql_query("create table students (roll_no int(10) not null, name varchar(30), class varchar(10), primary key(roll_no))",mydb)
# df =pd.read_sql_query("show tables",mydb)
sql_add_record="Insert into students (roll_no,name,class) values(%s,%s,%s)"
record1=(1, "Kavitha", "5th")
# pd.read_sql_query(sql_add_record,record1)
# mycursor.execute(sql_add_record,record1)
# mycursor.execute("select * from students")

# mycursor.execute("Alter table students drop primary_key(roll_no)")


########################################### Alter table adding new column to the table #########################################################
# mycursor.execute("Alter table students add place varchar(200)")

# mycursor.execute("Insert into students (roll_no,name,place) values(3,'kavitha','London')")
# df=pd.read_sql_query("select * from students",mydb)
# print(df)
############################################# Update Table modifying the value for a particular record #############################################

# mycursor.execute("update students set place='London' where name='Kavitha'")
mycursor.execute("Insert into students (roll_no,name,class,place) values(4,'Priya','9th','Tumkur')")
df=pd.read_sql_query("select * from students",mydb)
print(df)
# for record in mycursor:
#     print(record)
mydb.commit()
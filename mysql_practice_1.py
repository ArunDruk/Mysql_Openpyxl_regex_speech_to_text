import mysql.connector

################################################## Connecting to the Database ##################################################
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Feb@2020",
    database="test_db1"  # This tells python to point to the database test_db1
)

################################################## Initializing the Cursor through which we can access the database##################################################
mycursor=mydb.cursor()

################################################## Executing MySQL commands ##################################################
# mycursor.execute("create DATABASE test_db1")
#mycursor.execute("show databases")

################################################## To Print all the databases available ##################################################
# for db in mycursor:
#     print(db)
################################################## To Create Table inside the database ##################################################
#mycursor.execute("create table class_5th_students (name varchar(255), age integer(10))")
################################################## To display the tables inside the database "test_db1"##################################################
# mycursor.execute("show tables")
#
# for tb in mycursor:
#     print(tb)
################################################## Inserting a row or a record into the table "class_5th_students ##################################################
# sqlformula="INSERT INTO class_5th_students (name,age) VALUES(%s, %s)"
# student1=("Arun",18)
#
# mycursor.execute(sqlformula,student1)
# mydb.commit()
################################################## Querying the database ##################################################
# mycursor.execute("select * from class_5th_students")
# for query in mycursor:
#     print(query)

################################################## Inserting multiple rows or a record into the table "class_5th_students ######################################
# sqlformula="INSERT INTO class_5th_students (name,age) VALUES(%s, %s)"
# students=[("Swati",13),("Smitha",45),("Kavya",19)]
# mycursor.executemany(sqlformula,students)
# mydb.commit()
################################################## Querying the database ##################################################
# mycursor.execute("select * from class_5th_students")
# for query in mycursor:
#     print(query)
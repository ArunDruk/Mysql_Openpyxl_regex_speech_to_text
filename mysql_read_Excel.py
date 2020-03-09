import mysql.connector
import csv

mydb=mysql.connector.connect(host="localhost",user="root",passwd="Feb@2020",database="test1",auth_plugin="mysql_native_password")

mycursor=mydb.cursor()

###### Shows the tables present inside the database ##################
# mycursor.execute("show tables")
# for i in mycursor:
#     print(i)

########## Inserting record into Database ##################
# sql = "INSERT INTO customers1 (name, address) VALUES (%s, %s)"
#val = ("Simran", "caley")
#mycursor.execute(sql,val)

########## Read CSV file and taking to the Data variable which is list #################
# with open("SQL_data_values.csv",'r') as fr:
#     thereader=csv.reader(fr)
#     Data=list(thereader)

################## To calculate the length of rows and columns in the excel table ###############
#print(len(Data)) # Gives the length of rows or length of records
#print(len(Data[1]) # Gives the length of column

################## Inserting into DB the records which was read from the Excel #############
# for j in range(len(Data)):
#     sql = "INSERT INTO customers1 (name, address) VALUES (%s, %s)"
#     val=Data[j]
#     mycursor.execute(sql, val)


######### Query the Database and write the records to the Excel file #####################

mycursor.execute("select * from customers1")
with open("Db_values_to_csv.csv",'w',newline="") as fw:
    thewriter=csv.writer(fw)
    thewriter.writerow(["name","address"])
    for record in mycursor:
        thewriter.writerow(record)

# for record in mycursor:
#       print(record)

mydb.commit()
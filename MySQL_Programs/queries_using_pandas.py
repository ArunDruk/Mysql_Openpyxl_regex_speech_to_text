import mysql.connector
import pandas as pd
import csv

mydb=mysql.connector.connect(
    user="root",
    passwd="Feb@2020",
    host="localhost",  # This is going to be some URL, if you are connecting to some CLoud where the database resides
    database="db_03_jul_2020"
)

df=pd.read_sql_query("select * from users",mydb)
print(df)
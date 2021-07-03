# pip install cx-Oracle
# Need to install Oracle Instant client

import cx_Oracle
import os
os.environ['PATH']='E:\\app\\OracleHomeUser1\\instantclient_18_3'
########## To check below code is for python 32 or 64-bit ########
# import sys
# print("%x" % sys.maxsize, sys.maxsize > 2**32)
########## ########## ########## ########## ##########

# Establish connection to the database
con=cx_Oracle.connect("username","passwd","localhost/pdborcl")

cur=con.cursor()
query1="insert into student values(102,'Arun')"
query2= "delete student where sid=102"
cur.execute(query1)

cur.close()
con.commit()
con.close()

print("Completed!!")



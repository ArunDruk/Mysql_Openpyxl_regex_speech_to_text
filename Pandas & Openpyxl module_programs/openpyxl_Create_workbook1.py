# pip install openpyxl

from openpyxl import Workbook
import time

book1=Workbook()
sheet=book1.active

sheet['A1']=1500
sheet['B1']=2500
now=time.strftime("%x") # %X

sheet['C1']=now
book1.save("test1.xlsx")
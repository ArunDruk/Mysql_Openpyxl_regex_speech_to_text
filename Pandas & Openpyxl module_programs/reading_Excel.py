# Pandas module uses module xlrd -> to read excel files and xlwt -> to write excel files
# pip install xlrd
# pip install xlwt

import pandas as pd

excel_file="test_file.xlsx"
df=pd.read_excel(excel_file,sheet_name="SheetB",index_col=0) # either use the sheet name or the sheet number. Sheet numbers start with zero.

# print(df.head()) # Prints the top 5 rows by default or else pass the number of rows to print.
# print(df.tail()) # Prints the bottom 5 rows by default or else pass the number of rows to print.
print(df.shape)  # This prints the number of rows, columns in that excel sheet.
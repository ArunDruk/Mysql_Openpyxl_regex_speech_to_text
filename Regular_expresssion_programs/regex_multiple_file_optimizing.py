import re
from datetime import datetime

files = ["PS_401Bill_GL_CAUTO.txt","PS_FBB_GL_CAUTO.txt","PS_CAUTO_Accrual__BW191108.txt","PS_CAUTO_Accrual__WK191115.txt"]

str_20_len=datetime.now().strftime("%Y%m%d%H%M%S%f")
cur_date=datetime.now().strftime("%m/%d/%Y")

for file in files:
    Read_lines=[]
    Write_lines=[]
    with open(file,'r') as fr:
     Read_lines=fr.readlines()
     for line in Read_lines:
        date_modified_str=re.sub(r'\d{2}/\d{2}/\d{4}',cur_date,line)
        if(file=="PS_401Bill_GL_CAUTO.txt"):
           str_20_modified=re.sub(r'\d{20}',str_20_len,date_modified_str)
        elif(file=="PS_CAUTO_Accrual__BW191108.txt"):
           str_20_modified=re.sub(r'Accrual\sWBW191108\s\d{1,6}',str_20_len,date_modified_str)
        elif(file=="PS_CAUTO_Accrual__WK191115.txt"):
           str_20_modified=re.sub(r'Accrual\sWK191115\s\d{1,6}',str_20_len,date_modified_str)
        elif(file=="PS_FBB_GL_CAUTO.txt"):
           str_20_modified=re.sub(r'FLX\s0120\s\d{1,6}',str_20_len,date_modified_str)
        str_20_len=str(int(str_20_len)+1)
        Write_lines.append(str_20_modified)
    with open(file,'w') as fw:
       fw.writelines(Write_lines)

# Read_lines=[]
# Write_lines=[]
# with open("PS_CAUTO_Accrual__BW191108.txt",'r') as fr:
#     Read_lines=fr.readlines()
#     for line in Read_lines:
#         date_modified_str=re.sub(r'\d{2}/\d{2}/\d{4}',cur_date,line)
#         str_20_modified=re.sub(r'Accrual\sWBW191108\s\d{1,6}',str_20_len,date_modified_str)
#         str_20_len=str(int(str_20_len)+1) # The 20 digit number at the end in each record should have a unique number, so incrementing 1 for each record
#         Write_lines.append(str_20_modified)
#
# with open("PS_CAUTO_Accrual__BW191108.txt",'w') as fw:
#     fw.writelines(Write_lines)

# Read_lines=[]
# Write_lines=[]
# with open("PS_CAUTO_Accrual__WK191115.txt",'r') as fr:
#     Read_lines=fr.readlines()
#     for line in Read_lines:
#         date_modified_str=re.sub(r'\d{2}/\d{2}/\d{4}',cur_date,line)
#         str_20_modified=re.sub(r'Accrual\sWK191115\s\d{1,6}',str_20_len,date_modified_str)
#         str_20_len=str(int(str_20_len)+1) # The 20 digit number at the end in each record should have a unique number, so incrementing 1 for each record
#         Write_lines.append(str_20_modified)
#
# with open("PS_CAUTO_Accrual__WK191115.txt",'w') as fw:
#     fw.writelines(Write_lines)

# Read_lines=[]
# Write_lines=[]
# with open("PS_FBB_GL_CAUTO.txt",'r') as fr:
#     Read_lines=fr.readlines()
#     for line in Read_lines:
#         date_modified_str=re.sub(r'\d{2}/\d{2}/\d{4}',cur_date,line)
#         str_20_modified=re.sub(r'FLX\s0120\s\d{1,6}',str_20_len,date_modified_str)
#         str_20_len=str(int(str_20_len)+1)
#         Write_lines.append(str_20_modified)
#
# with open("PS_FBB_GL_CAUTO.txt",'w') as fw:
#     fw.writelines(Write_lines)
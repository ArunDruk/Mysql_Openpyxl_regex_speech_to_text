import re
from datetime import datetime

s="""
    A|MAN GLB US|Payroll|MAN:Payroll Accrual|11/08/2019|USD|||784.90| ||||||||
    ||||||||NOV-2019|00706|611010|1006|000|106|00000|0000||||Accrual WBW191108||
    ||||PR20191102 WBW191108 CAI ABA AREN200 E REG Regular Earnings|20200604185459486816||||||||||||||||||||
    
"""
# matches=re.finditer(r'\d{2}/\d{2}/\d{4}',s)
# matches=re.finditer(r'\d{20}',s)
# for match in matches:
#     print(match)

str_20_len=datetime.now().strftime("%Y%m%d%H%M%S%f")
cur_date=datetime.now().strftime("%m/%d/%Y")

Read_lines=[]
Write_lines=[]
with open("PS_CAUTO_Accrual__BW191108.txt",'r') as fr:
    Read_lines=fr.readlines()
    for line in Read_lines:
        date_modified_str=re.sub(r'\d{2}/\d{2}/\d{4}',cur_date,line)
        str_20_modified=re.sub(r'\d{20}',str_20_len,date_modified_str)
        str_20_len=str(int(str_20_len)+1) # The 20 digit number at the end in each record should have a unique number, so incrementing 1 for each record
        Write_lines.append(str_20_modified)

with open("PS_CAUTO_Accrual__BW191108.txt",'w') as fw:
    fw.writelines(Write_lines)



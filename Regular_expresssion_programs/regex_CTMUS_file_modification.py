import re
from datetime import datetime

acc_date=datetime.now().strftime("%m/%d/%Y")
acc_month_date=datetime.now().strftime("%b/%d/%Y")
acc_period=str(datetime.now().strftime("%b-%Y"))
acc_period=acc_period.upper()
str_20_len=datetime.now().strftime("%Y%m%d%H%M%S%f")

Read_lines=[]
Write_lines=[]
with open("CTMUS_0_A_MAY-2020_05.DAT",'r') as fr:
    Read_lines=fr.readlines()
    for line in Read_lines:
        date_modified_str=re.sub(r'\d{2}/\d{2}/\d{4}',acc_date,line)
        period_modified_str=re.sub(r'[A-Za-z]{3}-\d{2,4}',acc_period,date_modified_str)
        month_modified_str=re.sub(r'[A-Za-z]{3}/\d{2}/\d{2,4}',acc_month_date,period_modified_str)
        str_20_modified=re.sub(r'26071.{1,4}',str_20_len,month_modified_str)
        str_20_len=str(int(str_20_len)+1) # The 20 digit number at the end in each record should have a unique number, so incrementing 1 for each record
        Write_lines.append(str_20_modified)

with open("CTMUS_0_A_MAY-2020_05.DAT",'w') as fw:
    fw.writelines(Write_lines)

# given_str="A|MAN GLB US|CTM|Treasury|05/05/2020|USD||||557.90||||||||||||||||MAY-2020|00444|111120|0000|000|000|00000|0000||||Treasury Cash Sweep May/05/2020|Treasury Cash Sweep May/05/2020|||||Southern Cal Ford Fact Fund|260712||||||||||||||||||||"
# modified_str=re.sub(r'26071.{1,4}',str_20_len,given_str)
# print(modified_str)
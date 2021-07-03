import re
from datetime import datetime

gl_date=str(datetime.now().strftime("%d-%b-%Y")).upper()
inv_date=str(datetime.now().strftime("%d-%b-%y")).upper()
mon_yr=str(datetime.now().strftime("%b-%y")).upper()
jrnl_des=datetime.now().strftime("%M%S")


Read_lines=[]
Write_lines=[]
with open("ISGL_INTERCOMP_CAI_AUG-2020.txt",'r') as fr:
    Read_lines=fr.readlines()
    for line in Read_lines:
        gl_date_modified_str=re.sub(r'\d{2}-[A-Z]{3}-\d{4}',gl_date,line)
        inv_date_modified=re.sub(r'\d{2}-[A-Z]{3}-\d{2}',inv_date,gl_date_modified_str)
        mon_yr_modified=re.sub(r'AUG-20',mon_yr,inv_date_modified)
        jrnl_des_modified = re.sub(r'105782376', "10578"+jrnl_des, mon_yr_modified)
        Write_lines.append(jrnl_des_modified)
        # Write_lines.append(mon_yr_modified)

with open("ISGL_INTERCOMP_CAI_AUG-2020.txt",'w') as fw:
    fw.writelines(Write_lines)
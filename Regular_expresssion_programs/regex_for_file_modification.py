import re
from datetime import datetime,date
string="BL_5944	Actual	MAN GLB US	P&L and B/S Reclass	BlackLine	06/04/2020	444SB-Co-op Market 000 Reclass March 2020_BL_5944	444SB-Co-op Market 000 Reclass March 2020	No		1	00444	234520	0000	000	000	00000	0000			1380.45	Invoice Validated , Invoice Number: EXP-487616 , Invoice Date: 07-FEB-20 , Invoice Description: Element Super Bowl Event												USD			sbehailu"

#####################################################################################################################################################################
# pattern=re.compile(r'\d{2}/\d{2}/\d{4}')
#pattern=re.compile(r'^BL_\d{4}')
#
# matches=pattern.finditer(string)
#
# for match in matches:
#     print(match)

#ptrn=r'(0|1)[1-9]/[0-9]{2}/[0-9]{4}'
#####################################################################################################################################################################
# cur_date=date.today().strftime("%m/%d/%Y")
# cur_date=datetime.now().strftime("%m/%d/%Y")
# min_sec=datetime.now().strftime("%M%S")
# first_str="BL_"+str(min_sec)
# new_string=re.sub(r'(0|1)[1-9]/[0-9]{2}/[0-9]{4}',cur_date,string)
# modified_string=re.sub(r'^BL_\d{4}',first_str,new_string)
# print(modified_string)
#####################################################################################################################################################################
read_Lines=[]
write_Lines=[]
with open("MANGL_BLKLN_JE_EXTRACT.tsv",'r') as fr:
    read_Lines=fr.readlines()
    # write_Lines=fw.writelines(read_Lines)
    for line in read_Lines:
        cur_date = datetime.now().strftime("%m/%d/%Y")
        min_sec=datetime.now().strftime("%M%S")
        first_str="BL_"+str(min_sec)
        new_string=re.sub(r'(0|1)[1-9]/[0-9]{2}/[0-9]{4}',cur_date,line)
        modified_string=re.sub(r'^BL_\d{4}',first_str,new_string)
        write_Lines.append(modified_string)

with open("MANGL_BLKLN_JE_EXTRACT.tsv",'w') as fw:
    fw.writelines(write_Lines)



#print(L1)


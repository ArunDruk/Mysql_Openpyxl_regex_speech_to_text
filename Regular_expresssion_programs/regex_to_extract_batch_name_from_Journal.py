import re

s="BlackLine A 1147550 162797159"
# Lines=[]
# collections=[]
# with open("Journal Import.txt",'r') as fr:
#     Lines=fr.readlines()
#
# for line in Lines:
#     ptrn=re.compile(r'BlackLine\sA\s\d{7}\s\d{9}')
#     matches=ptrn.finditer(line)
#     for match in matches:
#         collections.append(match)
#
# print(collections)

# fo=open("Journal Import.txt","r")
# lines=fo.readlines()
# # print("Journal Imported Batch Name is : - "+lines[17][8:37].strip())
# batch_name=lines[17][8:37].strip()
# print(batch_name)

found=re.match(r'BlackLine\sA\s\d{7}\s\d{9}',s)
print(found)
print(found.group(0))
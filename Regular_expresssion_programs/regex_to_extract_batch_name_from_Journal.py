import re

s="BlackLine A 1147550 162797159"
Lines=[]
collections=[]
with open("Journal Import.txt",'r') as fr:
    Lines=fr.readlines()
count=1
for line in Lines:
    # print(count)
    ptrn=re.compile(r'BlackLine\sA\s\d{7}\s\d{9}')
    matches=ptrn.finditer(line)
    # count += 1
    for match in matches:
        matched_str= match.group()
        if matched_str !=None:
            break

print(matched_str)

# fo=open("Journal Import.txt","r")
# lines=fo.readlines()
# # print("Journal Imported Batch Name is : - "+lines[17][8:37].strip())
# batch_name=lines[17][8:37].strip()
# print(batch_name)

# found=re.match(r'BlackLine\sA\s\d{7}\s\d{9}',s)
# print(found)
# print(found.group(0))
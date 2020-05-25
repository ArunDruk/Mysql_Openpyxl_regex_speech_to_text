from datetime import datetime as dt
import time

def Read():
    with open("CoStar_INV_IS_US_2020.txt", 'r') as file:
        lines = [
            line.rstrip().replace('"', '').split("|")
            for line in file]
    return [dict(zip(lines[0], line))
            for line in lines[1:]]


List_of_dict=Read()

#print(List_of_dict)
L1=[]
for Dict in List_of_dict:

    for k in Dict.keys():
        if (k=='Invoice Description'):
            val=Dict[k]
            L1.append(val)

D2={}
L1=list(set(L1))
#str(int(dt.datetime.now().strftime("%Y%m%d%H%M%S
for index,Dict in enumerate(List_of_dict):
    for k,v in Dict.items():
        D2['Invoice Description']=v
       #  #for i in L1:
       # # while (Dict['Invoice Description']==i for i in L1):
       #      if Dict['Invoice Description']==i:
       #          Dict['Invoice Number']=str(int(dt.now().strftime("%Y%m%d%H"))+int(index))
       #      else:


print(D2)
#print(List_of_dict)
#print(L1)
#
# for Dict in List_of_dict:
#
#     for k in Dict.keys():
#         #if(k=='Invoice Number'):
#         if (k=='Invoice Description'):
#
#             for
#             Dict[k]="1988"
#         elif(k=='Invoice Date'):
#             Dict[k]="30/09/1988"

#print(List_of_dict)

def Write(rows):

    def return_str(row):
        return "|".join(map(str, [f'"{item}"'
        for item in row.values()]))+'\n'


    header = "|".join(map(str,[f'"{key}"' for key in rows[0].keys()]))

    with open("CoStar_INV_IS_US_2020.txt", 'w') as file:
        file.write(header+'\n')
        file.writelines("".join([return_str(row)
                                for row in rows]))


#Write(List_of_dict)
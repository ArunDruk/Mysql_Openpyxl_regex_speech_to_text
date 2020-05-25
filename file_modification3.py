def Read():
    with open("CoStar_GL_IS_US_2020.txt", 'r') as file:
        lines = [
            line.rstrip().replace('"', '').split("|")
            for line in file]
    return [dict(zip(lines[0], line))
            for line in lines[1:]]


List_of_dict=Read() # Returns list of Dictionary, Each row is one Dictionary.
val="1988"
#print(len(func_return))
#Dict1=func_return
# for Dict in Dict1:
#     #print(Dict['Journal_Line_ID'])
#     Dict['Journal_Line_ID']=val
#     val+=1
#
# for Dict in Dict1:
#     print(Dict['Journal_Line_ID'])

# for Dict in Dict1:
#     for k in Dict.keys():
#         print(Dict["Journal_Line_ID"])
#     break
last_count=1
for Dict in List_of_dict:
    print(last_count)
    for k in Dict.keys():
        if(k=="System_Lease_ID"):
            Dict[k]="1988"
        elif(k=="Journal_Entry_ID"):
            Dict[k]="1988"
        elif(k=="Accounting_Date"):
            Dict[k]="30/09/1988"
    if (last_count < len(List_of_dict)):
        Dict['Journal_Line_ID']=val #give the aqconvert.
        valu=int(val)+1 #Delay
        val=str(valu)
        last_count += 1

def Write(rows):

    def return_str(row):
        # return "|".join(map(str, [f'"{item}"'
        # for item in row.values()]))
        return "|".join(item for item in row.values())+'\n'

    #header = "|".join(map(str,[f'"{key}"' for key in rows[0].keys()]))
    header = "|".join(key for key in rows[0].keys())
    with open("CoStar_GL_IS_US_2020.txt", 'w') as file:
        file.write(header+'\n')
        file.writelines("".join([return_str(row)
                                for row in rows]))


Write(List_of_dict)
# Read()
# print(func_return[4])

# Dict1=func_return[1]
# #print(Dict1)
# print(Dict1['Accounting_Date'])
# print(Dict1['System_Lease_ID'])
# print(Dict1['Journal_Entry_ID'])
#'Journal_Name': '1864-ELEMENT'
#'Journal_Line_ID': '4477'
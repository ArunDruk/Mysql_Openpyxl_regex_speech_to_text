

def adding_list(given_list):
    new_list = []
    inc=1
    for pos in given_list:
        new_list.append(pos+inc)
        inc+=1
    return new_list


with open("CoStar_GL.txt","r") as fr:
    Data=fr.read()

    sys_lease_id_pos= [i for i in range(len(Data)) if Data.startswith("SLI_",i)]
    journal_entry_id_pos= [i for i in range(len(Data)) if Data.startswith("JEI",i)]
    journal_name_pos= [i for i in range(len(Data)) if Data.startswith("JN_",i)]
    acc_date_pos= [i for i in range(len(Data)) if Data.startswith("10/3",i)]
    Journal_Line_id_pos= [i for i in range(len(Data)) if Data.startswith("JLI6",i)]

sys_lease_id_pos=adding_list(sys_lease_id_pos)
journal_entry_id_pos=adding_list(journal_entry_id_pos)
journal_name_pos=adding_list(journal_name_pos)
acc_date_pos=adding_list(acc_date_pos)
Journal_Line_id_pos=adding_list(Journal_Line_id_pos)

print ("sys_lease_id_pos = ",sys_lease_id_pos)
print ("journal_entry_id_pos = ",journal_entry_id_pos)
print("journal_name_pos = ",journal_name_pos)
print("acc_date_pos = ",acc_date_pos)
print("Journal_Line_id_pos = ",Journal_Line_id_pos)

# sys_lease_id_pos =  [509, 876, 1208, 1527, 1845]
# journal_entry_id_pos =  [523, 890, 1222, 1541, 1859]
# journal_name_pos =  [529, 896, 1228, 1547, 1865]
# acc_date_pos =  [614, 980, 1311, 1632, 1949]
# Journal_Line_id_pos =  [670, 1025, 1352, 1672, 2008]

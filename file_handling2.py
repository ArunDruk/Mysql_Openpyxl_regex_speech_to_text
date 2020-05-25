with open("CoStar_GL.txt","r+") as fr:
    Data=fr.read()

#for j in range(1,6):
    sys_lease_id_pos= [i for i in range(len(Data)) if Data.startswith("SLI_",i)]
    journal_entry_id_pos= [i for i in range(len(Data)) if Data.startswith("JEI",i)]
    journal_name_pos= [i for i in range(len(Data)) if Data.startswith("JN_",i)]
    acc_date_pos= [i for i in range(len(Data)) if Data.startswith("10/3",i)]
    Journal_Line_id_pos= [i for i in range(len(Data)) if Data.startswith("JLI6",i)]

print ("sys_lease_id_pos = ",sys_lease_id_pos)
print ("journal_entry_id_pos = ",journal_entry_id_pos)
print("journal_name_pos = ",journal_name_pos)
print("acc_date_pos = ",acc_date_pos)
print("Journal_Line_id_pos = ",Journal_Line_id_pos)




# sys_lease_id_pos=(509,876,1208,1608,1845)#(530,917,1269,1608,1946)
# journal_entry_id_pos=(523,890,1222,1622,1859)
# journal_name_pos=(529,896,1228,1628,1865)
# accounting_date_pos=(614,980,1311,1713,1949)
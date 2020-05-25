# sys_lease_id_pos=(509,876,1208,1608,1845)#(530,917,1269,1608,1946)
# journal_entry_id_pos=(523,890,1222,1622,1859)
# journal_name_pos=(529,896,1228,1628,1865)
# accounting_date_pos=(614,980,1311,1713,1949)
# journal_line_id_pos=-

sys_lease_id_pos =  [509, 876, 1208, 1527, 1845]
journal_entry_id_pos =  [523, 890, 1222, 1541, 1859]
journal_name_pos =  [529, 896, 1228, 1547, 1865]
acc_date_pos =  [614, 980, 1311, 1632, 1949]
Journal_Line_id_pos =  [670, 1025, 1352, 1672, 2008]

with open("Original_file.txt","r+") as fr:
    fr.read()
    for i in sys_lease_id_pos:
        fr.seek(i,0)
        fr.write("Arun")
    for i in journal_entry_id_pos:
        fr.seek(i,0)
        fr.write("Arun")
    for i in journal_name_pos:
        fr.seek(i,0)
        fr.write("Arun")
    for i in acc_date_pos:
        fr.seek(i,0)
        fr.write("Arun")
    for i in Journal_Line_id_pos:
        fr.seek(i, 0)
        fr.write("Arun")

# Data1=f1.read()
# print(Data1)
# # f1.seek(701,0)
# # f1.write("Arun")
# # f1.seek(778,0)
# # f1.write("Arun")
# # f1.seek(973,0)
# # f1.write("Arun")

# L=(100,145,180)
# for i in L:
#     f1.seek(i,0)
#     f1.write()


# fo.write(sys_lease_id_line)
# #      fo.seek(566,0)
# #      fo.write (journal_entry_id_line)
# #      fo.seek(571,0)
# #      fo.write (journal_name_line)
# #      fo.seek(701,0)
# #      fo.write (accounting_date)
# #      fo.seek(778,0)
# #      fo.write (journal_id_line1)
# #      fo.seek(973,0)




# sys_lease_id_line = aqConvert.DateTimeToFormatStr(aqDateTime.Now(),"%S%M")
#      journal_entry_id_line = aqConvert.DateTimeToFormatStr(aqDateTime.Now(),"%S%M")
#      journal_name_line = aqConvert.DateTimeToFormatStr(aqDateTime.Now(),"%S%M")
#      accounting_date = aqConvert.DateTimeToFormatStr(aqDateTime.Now(),"%m/%d/%Y")
#      journal_id_line1 = aqConvert.DateTimeToFormatStr(aqDateTime.Now(),"%S%M")
#      journal_id_line2 = aqConvert.DateTimeToFormatStr(aqDateTime.Now(),"%M%S")
#      fo=open(file_name,"r+")
#      lines=fo.readlines()
#      fo.close()
#      fo=open(file_name,"r+")
#      data=fo.read()
#      fo.seek(512,0)
#      fo.write(sys_lease_id_line)
#      fo.seek(566,0)
#      fo.write (journal_entry_id_line)
#      fo.seek(571,0)
#      fo.write (journal_name_line)
#      fo.seek(701,0)
#      fo.write (accounting_date)
#      fo.seek(778,0)
#      fo.write (journal_id_line1)
#      fo.seek(973,0)
#      fo.write(sys_lease_id_line)
#      fo.seek(1027,0)
#      fo.write (journal_entry_id_line)
#      fo.seek(1032,0)
#      fo.write (journal_name_line)
#      fo.seek(1163,0)
#      fo.write (accounting_date)
#      fo.seek(1232,0)
#      fo.write (journal_id_line2)

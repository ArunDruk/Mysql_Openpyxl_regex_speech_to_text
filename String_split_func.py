import re
msg= "Note APP-OFA-4826675: Transaction saved for asset number 3201617.  Reference numbers:  1376525, 1376526"

# match=re.search(r'\s\d{7}',msg)
# print(match.group().strip())
# print(match.group())
#
# s="3201617."
# print(s)
# print(s[:-1])

msg1=msg[10:]
print(msg1)

# conf_msg=msg.split(".")[0][-7:]
# # asset_num=conf_msg.split(" ")[-1]
# print(conf_msg)
# # print(asset_num)
#
# asset_no=conf_msg.split(".",2)[0][-7:]
# print(asset_no)


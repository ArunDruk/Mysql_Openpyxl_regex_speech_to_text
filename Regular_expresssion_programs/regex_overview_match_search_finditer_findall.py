import re
# match checks for a match only at the beginning of the string, while search checks for a match anywhere in the string
# Python regex search() stops at the first match
s='''192.24.7.48
    172.64.17.8
    10.4.6.23
    port=5060
    (456-987-143)
    '''
########################## Search ###############################################################
# ip_addr=re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',s)
# print(ip_addr.group())
############################ Match ##############################################################################
# ip_addr=re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',s)
# print(ip_addr.group())
################################ Compile ##########################################################################
# ptrn=re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
# ptrn=re.compile(r'\(\d{3}-\d{3}-\d{3}\)')
################################# Using Compile findall #########################################################################
# matches=ptrn.findall(s)
# print(matches)
################################# Using Compile finditer #########################################################################
# matches=ptrn.finditer(s)
# for match in matches:
#     print(match.group())
################################### finditer #######################################################################
# matches=re.finditer(r'\(\d{3}-\d{3}-\d{3}\)',s)
# matches=re.finditer(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',s)
# for match in matches:
#    print(match.group())
######################################## findall ###########################################################################
matches=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',s)
#print(matches)
with open("Ip_list.txt",'w') as fw:
    for match in matches:
        fw.writelines(match+'\n')
######################################################################################################################################################
import re

string="""
    080-37421834
    044-14572534
"""
# ptrn=re.compile(r'(\d{3}-)?\d{4}-\d{4}')
# ph_num=ptrn.search("This is my number 3742-1834")
# print(ph_num.group(0))
####################################################################################################
# w : represents word character which is alphanumeric, underscore
# W: represents which is not alphanumeric
# s : represents a single whitespace, newline, tab falls under this category.
####################################################################################################
# ptrn=re.compile(r'\w+\s\w+')
# bat_regex=ptrn.search("Come on Bat man")
# print(bat_regex.group())
############################### TO find digit space and a word character multiple occurance and put in a list #############
# ptrn=re.compile(r'\d+\s\w+')
# list_items=ptrn.findall("4 apples, 9 bananas and 15 mangoes")
# print(list_items)
################################ TO find Hello at the End of the String##############################################
ptrn=re.compile(r'Hello$')
found=ptrn.search("Arun Says Hello")
print(found.group())
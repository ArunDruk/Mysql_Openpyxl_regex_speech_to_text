import re

# These are the MetaCharacters and need to be escaped with blackslash '\'
#  .[{()\^$|?*+

s= """
    pineapple
    wine
    kine
    dining
    finer
    Ha HaHa
    cat
    bat
    pat
    mat
    """
# re.compile(r'[^[b]at')
# ptrn=re.compile(r'[^[w][ia].+')
ptrn=re.compile(r'[^p]at')
# ptrn=re.compile(r'\BHa\b') # Matches the last 'Ha' as there is no word boundary(\B) at the starting of the string and there is a word boundary at the end of the string
# ptrn=re.compile(r'\bHa\B')
matches=ptrn.finditer(s)
for match in matches:
    print(match)

# ret_val=re.subn(r'\w+',"Hello",s)
# print(ret_val)


import re

txt="""
    abcd
    bfcd
    352-980-879    
    123.436.908
    675*576*894
    800-980-879 
    900-980-879
    Mr.Dragon
    Mr.Cheetah
    Mr. Tiger
    Mr L
    Ms.Divya
    Mrs Savithri
    arunbond30@skype.com
    arunbond30@skype*com
    arun.s.kumar@techmahindra.com
    arun&43@example.com
    arun.teacher@cap.org
    http://www.google.com
    https://www.msn.com
    http://youtube.org
    """

#ptrn=re.compile(r'\d{3}[-]\d{3}[-]\d{3}')
#ptrn=re.compile(r'Mr\.?\s?[a-zA-Z]\w*')
# ptrn=re.compile(r'M(r|s|rs)\.?\s?[a-zA-Z]\w*')  #This is called groups()
#ptrn=re.compile(r'(Mr|Ms|Mrs)\.?\s?[a-zA-Z]\w*') # The above one and this both are same
# ptrn=re.compile(r'[a-zA-Z][a-zA-Z0-9-.]+@[a-zA-Z]+\.(in|com)') # To match the mail ID's
#ptrn=re.compile(r'https?://(www\.)?[a-zA-Z]+\.[a-zA-Z]{2,10}') # To match the websites.

ptrn=re.compile(r'https?://(www\.)?(\w+)\.(\w+)') #To match the websites by Corey Schafer using word character.

matches=ptrn.finditer(txt)
##########################################################################
# Using Quantifiers to Match more than one Character.
# Qunatifiers:
# letter . is called as a Period, \. Period escaped with the backslash
##########################################################################
# * - 0 or more
# + - 1 or more
# ? - 0 or One - This symbol is used for optional use, we may need or may not need that character
# {3} - Exact number
# {3,5} - Range of numbers(minimum, maximum)
##########################################################################
L1=[]
for match in matches:
    L1.append(match.group(1)) # Group(0) is entire match, group(1) is www, 2 is domain name, 3 is top level domain names
print(L1)
######################### Groups ##########################
# () -> Groups allow us to match several other patterns
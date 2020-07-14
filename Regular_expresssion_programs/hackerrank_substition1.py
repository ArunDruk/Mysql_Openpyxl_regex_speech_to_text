# To remove or delete an empty line, use strip("\n")

import re

s="""10
x  && &   &x
x&|&&|&| ||x
x| |&&|  &&x
x& &   &| &x
x& &&&&||| x
x&|&  |    x
x &  & |&&&x
x|&|& &    x
x & &|| &||x
x |&|&&|&||x"""
# print(s)
sub1=re.sub(r'\d{1,3}',"",s)
sub2=sub1.strip("\n")
sub3=re.sub(r'\s&&\s'," and ",sub2)
sub4=re.sub(r'\s\|\|\s'," or ",sub3)


print(sub4)


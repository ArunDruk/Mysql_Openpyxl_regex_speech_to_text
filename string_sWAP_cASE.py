############################## Print the lower case characters into upper case and vice versa ########################################################################
import string
s ="HaCkErRank.com pREsenTs PythOnist 2"
chars=string.ascii_uppercase
new_string=""

for i in s:
    if i in chars:
        new_string=new_string+i.lower()
    else:
        new_string = new_string + i.upper()

print(s)
print(new_string)

######################################################################################################
# ar = list(map(int, input().rstrip().split()))  # To convert the input taken from the user into a list
#
# print(s1)
# print(L1)
# L1=[6523473246, 56134145, 75213412, 423576212]
# print(sum(L1))
# print(a)



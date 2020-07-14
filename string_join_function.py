
############################################# Example 1: #######################################################
# s= "thank you for choosing the Olympus dictation management system"
# L1=s.split()
#
# s1=" ".join (i for i in L1)
# print(s1)

# return (" ".join(pieces[i:i + n]) for i in range(0, len(pieces), n)

################################################ Example 2: ####################################################
import random
import string

nums=string.digits
Age_list=[]

for i in range(11):
    # Ages="".join(val for k in range(2) for val in str(random.choice(nums)))
    Ages="".join(random.choice(nums) for k in range(2))
    Age_list.append(Ages)

print(Age_list)

############################################ Example 3: ########################################################
# import string
# import random
#
# char=string.ascii_lowercase
# counter1="".join((random.choice(char) for i in range(6)))
# print(counter1)
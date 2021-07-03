######################################################################################################################################################
############################################################ Method 1 : using Set ##########################################################################################

# L=[1,2,2,3,3,3,4,4]
# L1=list(set(L))
# print (L1)

#####################################################################################################################################################
############################################################ Method 2 : using Ordered Dictionary ##########################################################################################
# from collections import OrderedDict
# L=[1,2,2,3,3,3,4,4]
#
# L1=list(OrderedDict.fromkeys(L))
# print(L1)
#####################################################################################################################################################
############################################################ Method 3 : using for loop ##########################################################################################
L=[1,2,2,3,3,3,4,4]
L1=[]
# for i in L:
#     if i not in L1:
#         L1.append(i)
[L1.append(i) for i in L if i not in L1]  # Using List Comprehension
print(L1)
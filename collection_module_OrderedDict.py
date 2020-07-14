from collections import OrderedDict
# Python OderDict, remembers the order in which the key-value pairs were added
o1=OrderedDict()
o1['a']=11
o1['z']=44
o1['c']=22

print(o1)

o1.move_to_end('a') # This will move the item mentioned to the end of the dictionary
print(o1)

popped_item=o1.popitem() # pop item will remove the last element from the dict and it will return it.
print(popped_item)
print(o1)

o1.popitem(last=False) # If last=False is given it will pop the first element
print(o1)


##############################################  Nornal dictionary verifying the order of Key-value pair ######################################################

# o2=dict()
# o2['a']=11
# o2['z']=44
# o2['c']=22
#
# print(o2)
####################################################################################################

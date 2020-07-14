
# You can use super().__MethodName__() to call that method from the base class, used in child class

###################################################################### Single Inheritance ######################################################################
# x=0
# class vehicle():
#     def __init__(self):
#         global x
#         x+=1
#         print("I'm from Vehicle class")
#
#
# class two_wheeler(vehicle):
#     def __init__(self):
#         super().__init__()
#         global x
#         x+=2
#         print("I'm from two_wheeler class")
#
# Gladiator=two_wheeler()
# print(x)

###################################################################### Multiple Inheritance ######################################################################
# When we search for an attribute in a class that is involved in python multiple inheritance, an order is followed.
# First, it is searched in the current class. If not found, the search moves to parent classes.
# This is left-to-right, depth-first.
# class vehicle():
#     def __init__(self):
#         print("I'm from Vehicle class")
#
#
# class two_wheeler():
#     def __init__(self):
#         print("I'm from two_wheeler class")
#
# class enfield(vehicle,two_wheeler):
#     def __init__(self):
#         super().__init__()
#         print("I'm from Enfield class")
#
#
# Thunder_bird=enfield()
# print(enfield.mro())  # Method resolution order will be first the child class then from left to Right in the order it is being inherited
# print(enfield.__mro__)

############################################################################################################################################

###################################################################### Multi-level Inheritance ######################################################################
# class A:
#     x = 1
#     print(x)
#
# class B(A):
#     pass
#
# class C(B):
#     pass
#
# cobj = C()

##################################################################   Hierarchical Inheritance ##########################################################################

# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(A):
#     pass
#
# print(issubclass(B, A) and issubclass(C, A))

####################################################################################################################################################
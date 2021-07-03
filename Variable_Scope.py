
#################################################### Illustration: 1 (Defining global and local variables) ################################################
# name = "Global"  # Variable defined outside a function block is called as a Global variable
#
# def variable_1():
#     name="local"  # Variable defined inside a function block is called a local variable
#     return name
#
# print(name)
# print(variable_1())
# print(name)
########################################################################################################################################################################################################
#################################################### Illustration: 2 (modifying the global variable inside the function block) ################################################
# name = "Global"
#
# def variable_1():
#     global name # This means you are referring to the Global variable name
#     name="Local"  # Now the Global variable name is been modified to Local
#     return name
#
# print(name)
# print(variable_1())
# print(name)
########################################################################################################################################################################################################
#################################################### Illustration: 3 (modifying the global variable inside the function block and also with the same variable name creating a local variable) ################################################
# name = "Global"
#
# def variable_1():
#     globals() ["name"]= "Modified Global variable" # This means you are referring to the Global variable name
#     name="Local"  # Now the Global variable name is been modified to Local
#     return name

# print(globals().values())
#
# print(name)
# print(variable_1())
# print(name)
########################################################################################################################################################################################################
########################################## Decorator Calling using the simple / normal method #################################
# def decor(func):
#     def wrap():
#         print("$$$$$$$$$$$$$$$$$$")
#         func()
#         print("$$$$$$$$$$$$$$$$$$")
#     return wrap
#
# def say_hello():
#     print("Hello Arun")
#
# new_func=decor(say_hello) # Different way of calling decor function
#
# new_func()

#################################### Decorator calling using Pie Syntax ####################################################
# def decor(func):
#     def wrap():
#         print("$$$$$$$$$$$$$$$$$$")
#         func()
#         print("$$$$$$$$$$$$$$$$$$")
#     return wrap
#
# @decor
# def say_hello():
#     print("Hello Arun")
#
# say_hello()
################################################################################################################################################################################
##################################### Returning inner func object and accessing inner func #####################################
# def outer_func():
#     def inner_func():
#         print("Am from inner func")
#     return inner_func
#
#
# func=outer_func()
#
# func()

####################################################################################################################################################
################################################ Passing some values in function ####################################################
# def divide(a,b):
#     return a/b
#
# def decor(func):
#     def wrap(a,b):
#         if b==0:
#             print("Can't divide by 0 or Zero")
#             return
#         return (a/b) #  return divide(a,b), you can also call the function instead of directly returning the value
#     return wrap
#
# func=decor(divide)
# print(func(11,5))
########################################################################################################################################################
###################################### Python Closure ##############################################################
# msg= "Hello Arun"
#
# def outer_fun(msg1):
#     def inner_fun():
#         print(msg1)
#     return inner_fun()
#
# outer_fun(msg)

####################################################################################################################


# def decor(func):
#     def wrap(a,b):
#         if b==0:
#             print("Can't divide by 0 or Zero")
#             return
#         return divide(a,b)
#     return wrap
#
# @decor
# def divide(a,b):
#     return a/b
#
# a=divide(11,2)
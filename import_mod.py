import int_float_validation
var1=int_float_validation.func1()
for i in var1:

    comp_name=i[:-2]
    mod = __import__(comp_name)
# print(mod) # <module 'json_format' from 'C:\\Users\\akumar6\\PycharmProjects\\Practice_programs\\json_format.py'>

obj=getattr(mod,comp_name,"No matching name found")

print(obj)

# class sample1():
#     def __init__(self,var1):
#         self.var1=var1
#
#     def public_method(self):
#         print("Going to call private method")
#         self.__private_method()
#
#     def __private_method(self):
#         print("this is from Private method")
#
# a=sample1()



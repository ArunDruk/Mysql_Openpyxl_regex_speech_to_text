# class employee():
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#
#     def emp_basic_info(self):
#         print("Employee full name is",self.fname+' '+self.lname)
#         print("Employee Email ID is",self.fname+'.'+self.lname+"@techm.com")
#
# emp1=employee("Arun","Dravid")
# emp2=employee("kiran","Tendulkar")
#
#
# class business_unit1(employee):
#     def badge_no(self,num):
#         print(f'The employee name is {self.fname+self.lname} and his badge num is {num}')
#
# Emp1=business_unit1("Arun","Dravid")
#
# Emp1.badge_no("3425")
#################################### Creating a Package ################################################################
# from package_1 import func1
# from package_1.my_sub_pkg1 import func2
# from package_1.my_sub_pkg1.func2 import mul_func
#
# a=func1.add_func()
# print(a)
#
# b=mul_func()
# print(b)
#
# c=func2.div_func()
# print(c)
######################################################################################################################################################

L=[1,2,3,4,5,6]
L1=L[1:]
print(L1)
L1=L[:-2]
print(L1)
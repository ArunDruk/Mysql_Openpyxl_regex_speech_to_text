#given_str="1,500.00"
# given_str="150.00"
#
# wanted_str=given_str.replace(",","").replace(".00","")
# print(wanted_str)

#cmp_Str="150"

# if (int(wanted_str)>0):
#     print("The tax component is validated")
# else:
#     print("Not able to validated the tax component")

from package_1 import func1
#import inspect

#print(dir(func1))
#print(inspect.getmembers(func1))

#print(f for f in inspect.getmembers(func1) if inspect.isfunction(f[1]))

print(func1.__all__)
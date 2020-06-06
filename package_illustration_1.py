from package_1 import func1
from package_1.my_sub_pkg1 import func2
from package_1.my_sub_pkg1.func2 import mul_func

a=func1.add_func()
print(a)

b=mul_func()
print(b)

c=func2.div_func()
print(c)
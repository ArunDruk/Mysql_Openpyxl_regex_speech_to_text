
# The @classmethod decorator can be applied on any method of a class. This decorator will allow us to call that method using the class name instead of the object / instance name.
# In the below example "person" is the class name, p1 and p2 are the objects or instances of the class "Person" ..
# Below we are calling the method_1 and method_3 using the class name "person"
class person:
    def __init__(self,a,b):
        self.a=10
        self.b=20

    @classmethod
    def method_1(self,a,b):
        print("The Sum of a+b is",a+b)

    def method_2(self,a,b):
        print("THe product of a x b is",a*b)

    @classmethod
    def method_3(self,a=1,b=3):
        print("This is from method_3")


p1=person(50,7)
p2=person(20,5)

person.method_1(7,5)

person.method_3()
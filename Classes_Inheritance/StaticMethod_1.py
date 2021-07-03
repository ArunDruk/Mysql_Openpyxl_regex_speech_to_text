
# A static method doesn't receive any reference argument whether it is called by an instance of a class or by the class itself.
class person:
    def __init__(self,a,b):
        self.a=10
        self.b=20

    @staticmethod
    def method_1(self,a,b):
        print("The Sum of a+b is",a+b)

    def method_2(self,a,b):
        print("THe product of a x b is",a*b)

    @classmethod
    def method_3(self,a=1,b=3):
        print("This is from method_3")


p1=person()
p2=person(20,5)

p1.method_1(7,5)

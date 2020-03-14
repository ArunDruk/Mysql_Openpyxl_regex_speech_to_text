
class parent():

    def __init__(self):
        print("I'm from Parent class")

class child1():

    def __init__(self):
        #super().__init__() # This will inherit the init method of the parent/Super class
        print("I'm from Child1 class")
        #print(child1.__mro__)

class child2(parent,child1):

    def __init__(self):
        parent.__init__(self)
        child1.__init__(self)
        print("I'm from Child2 class")


A=child2()
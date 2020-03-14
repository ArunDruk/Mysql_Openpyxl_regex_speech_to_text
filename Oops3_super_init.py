class parent():

    def __init__(self):
        print("I'm from Parent class")
        #super(parent,self).__init__()

class child1():

    def __init__(self,value):
        #super(child1,self).__init__() # This will inherit the init method of the parent/Super class
        print("I'm from Child1 class")
        self.value=10
        print(self.value)

class child2(parent,child1):

    def __init__(self):
        #super(child2,self).__init__()
        super(parent,self).__init__()
        print("I'm from Child2 class")
A=child2()
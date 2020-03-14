
class parent():

    def __init__(self):
        print("I'm from Parent class")

    def login(self):
        print("This login is from Parent class")

class child1(parent):

    def __init__(self):
        super().__init__()
        print("I'm from Child1 class")

    def login(self): # Child 1 is also having login method and parent class is also having a login method
        print("This login is from Child1 class")
        super().login() # This calls the login method of super/parent class

A=child1()

A.login()

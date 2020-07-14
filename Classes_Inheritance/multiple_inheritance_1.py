class parent_A():
    def __init__(self,text):
        print("This statement from Parent_A")
        add_text = "from Parent A :" +"'"+text+"'"
        print(f"{add_text}")
        print("*************************")
        super().__init__(text)  # This will call the init method of parent B


class parent_B():
    def __init__(self,text):
        print("This statement from Parent B")
        add_text="from Parent B "+text
        print(f"{add_text}")


class parent_C(parent_A,parent_B):
    def __init__(self,text):
        print("This statement from Parent C")
        print("*************************")
        super().__init__(text)  # This will call the init method of Parent A
        print("*************************")
        print("End of Parent C")


obj1=parent_C("Hello ARUN")
print(parent_C.mro())
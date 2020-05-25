
# Create Node
# Create Linked list
# Add nodes to linked list
# Print linked list

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_list():
    def __init__(self):
        self.head=None

    def insert(self,newNode):
# head => John => None;
        if self.head is None:
            self.head=newNode
# head => John => Ben => None || John => Mathew
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode

    def printList(self):
# head => John => Ben => Mathew
        if self.head is None:
            print("List is empty")
            return
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode=currentNode.next

#Node =>data,next
#firstNode.data=John, firstNode.next=None

firstNode=Node("Arun")
link_list=Linked_list()
Linked_list.insert(firstNode)

secondNode=Node("Kiran")
Linked_list.insert(secondNode)

thirdNode=Node("Daddy")
Linked_list.insert(thirdNode)

Linked_list.printList()
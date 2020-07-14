
# An object is any real-world entity that has attributes and behaviors.
# Anything in python programming Language is an object.
# we use ‘self’ to be able to refer to the object we’re dealing with
#  self parameter is to tell the interpreter to deal with the current object.

class fruits():
    def __init__(self,color, shape):  # __init__ has two attributes color and shape.
        self.color=color
        self.shape=shape

    def identity(self):  # The functions inside a Class object are called as Methods
        print(f"I'm in {self.color} color and {self.shape} shape")

orange=fruits("orange","round")  # Object Creation 'Orange' and passing arguments
grapes=orange  # Assigning orange object to grapes using assignment operator

orange.identity()
# del orange
#
# grapes.identity()
# print(grapes.color)

print(fruits.__doc__)

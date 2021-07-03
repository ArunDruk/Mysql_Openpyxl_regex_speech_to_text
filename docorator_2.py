
def decorate_func(func1): # the function which has to be decorated is passed as an Argument
    def wrap_func(): # This function enhances the functionality
        print("Hello students, today we are going to see:")
        return func1() # Calling the actual function
    return wrap_func


@decorate_func
def func1():
    print("Illustration of Decorator function")


func1()
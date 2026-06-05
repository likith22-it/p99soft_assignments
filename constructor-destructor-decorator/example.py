# Decorator in python - Decorator is a function in python
# that wrap other function or class within it to
# extend the functionality without changing the code

# constructor is used to initialize the object , objects can be invoced with the help 
# of __init__ method ,and also automatically open the files ,connect to databases,
# and we can even pass the external object as a instance where we call it as a dependency injection,
# it is a special function used to call automatically when object is created
# This method is responsible for creating a new instance of a class. It allocates
#  memory and returns the new object. It is called before __init__.


# Destructor Defined by the __del__ method, destructors are called when an object
# is about to be destroyed or garbage collected, it is used for resource clean
# (deleting the object or moving it into the garbage collection,)


def decorator(func):
    def wrapper(self):
        print("Before calling the function.")
        func(self)
        print("After calling the function.")
    return wrapper


class Student:
    def __init__(self, id, name, clg):
        self.id = id
        self.name = name
        self.clg = clg

    @decorator 
    def greet(self):
        print("Hello, Students!")


    def displayStudent(self):
        print("ID:", self.id, "Name:", self.name, "College:", self.clg)

    def __del__(self):
        print("Destructor called, object deleted")
    


s1 = Student(101, "Likith", "ABC College")
s1.displayStudent()
s1.greet()
del s1
s1.displayStudent()





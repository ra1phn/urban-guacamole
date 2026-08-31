"""
They are a powerful tool for modifying
or extending the behaviour of funtions
or methods without chanign their code. 
"""

"""
A decorator function should take another function
as an arguement/parameter.
It should have a wrapper function.
This function should be able to call the passed function.()

to use a decorator, you use
@<decorator function> before function definition

"""

def my_deco(func):
    def wrapper():
        print("Before we call the function")
        func()
        print("After we call the function")
    return wrapper

@my_deco
def hello():
    print("Hello world function executes")
    print("Hello world")

@my_deco
def french_hello():
    print("French Hello function")
    print("Bonjour world")

    # french_hello then my_deco

hello()

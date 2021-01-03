# Higher Order Function HOF
# HOF is a function that accepts a function as parameter
def greet(func):
    func()
# OR returns a function
def greet2():
    def func():
        return 5
    return func

# DECORATOR supercharge a function
# Wraps another function and enhances it or changes it



def my_decorator(func):
    def wrap_func():
        print("*********")
        func()
        print("*********")
    return wrap_func

# @my_decorator   #BY just using this syntax i can apply this extrafunctionality to any function
def hello():
    print("hellooooooo")
@my_decorator
def buy():
    print("see you later")

# hello()
# buy()

# Under the hood it works like this
hello2 = my_decorator(hello)  # the @decorator wraps around the hello function
                              # @decorator is the same as my_decorator(hello)()
                              # becase decorator(hello) return wrap_func, and then we call it with wrap_func()
hello2()

def my_decorator(func):
    def wrap_func(message):
        print("*********")
        func(message)
        print("*********")
    return wrap_func

@my_decorator   #BY just using this syntax i can apply this extrafunctionality to any function
def hello(greeting):
    print(greeting)

hello("blink")
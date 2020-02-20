def print_users(user,*users):
    print('First user argument: ', user)

    for user in users:
        print('user recieved from variable argument: ', user)

print_users('edureka','admin','cdeo','konsult')


def myFunction(arg1,arg2, arg3, *args, **kwargs):
    print('First normal argument: ' + str(arg1))
    print('second normal argument: ' + str(arg2))
    print('third normal argument: ' + str(arg3))
    print('Non-Keyworded arguments: ' + str(args))
    print('Keywordes arguments: ' + str(kwargs))

myFunction(1,2,3,4,5,6,7, name='Mandar', country='Sweden', age=24)
myFunction(ocupation='engineer')
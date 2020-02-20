def print_users(user,*users):
    print('First user argument: ', user)

    for user in users:
        print('user recieved from variable argument: ', user)

print_users('edureka','admin','cdeo','konsult')
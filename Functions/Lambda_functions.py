my_list = range(16)
# print a list that filter out the number not evenly divided by 3, so print only the number evenly divided by 3
print(list(filter(lambda x: x % 3 == 0, my_list)))

languages = ["HTML", "JavaScript", "Python", "Ruby"]
# Print a list with the word 'Python' if is in the languages list, filter out everything else
print(list(filter(lambda word: word == 'Python', languages)))

squares = [x ** 2 for x in range(1, 11)]
# print a list with the squares numbers between 30 an 70
print(list(filter(lambda big_squares: 30 < big_squares < 71, squares)))

# Thi will print out another secret message after filter out the X:s in the phrase
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = list(filter(lambda x: x != 'X', garbled))
print(''.join(message))

# this will take the  list in items and map ever x in item to squared them or cube them.
# Save it as a new list and asign them to the variable squared or cubed
items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))
cubed = list(map(lambda x: x ** 3, items))
print(squared)
print(cubed)
print(items)

# reduce takes a list as argument apply some operation to it and return a single output
from functools import reduce

# it will reduce the value from 4 to 3 to 2 to 1. same as x-- from 4 to 1 and save the result to y ever time it iterates
'''
same as:
def product():
    x=[1,2,3,4]
    y=1
    for item in x[::-1]:
        y *=item
    return y


But only in one line!!!!
'''
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(" this is the reduce")
print(product)

'''
Another example

squared = reduce(lambda x,y:(x**2)*y,[1,2,3,4])
print(squared)

Are the same as :


def squared2():
    x=[1,2,3,4]
    y=1
    for item in x[::-1]:
        y *=(item**2)
    return y
print(squared2())
'''

# list sorting using the second key example (0,2) the x[1]= 2
a= [(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda x: x[1]) # for every tuple exampe (0,2) return the key at index x[1]
print(a)
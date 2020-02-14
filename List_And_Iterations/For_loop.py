    # #Factorial = n(n-1)(n-2)(n-3).....1 med input from the user

'''

This is my own program that is very messy

'''

# #Promot the user and initialise start variable and empy array factorial[]
# n = int(input('Please ener the number of !n: '))
# i=0
# factorial=[]
#
# # fill the array with the n variables
# while i < n:
#     factorial.append(n)
#     n -= 1
#     print(factorial)

# #go trought he array and store the value in indexcounts -1 in relust variable then store the total in total after calculation
#
# print('This is factor: ',factorial)
# results =1
# total=1
# for counts in factorial:
#     results = (counts - 1)
#     if results !=0:
#         total *= results
# print(total*factorial[0])

""" Beautiful Solution
 Factorial function  with returninng a call to the same function until n! =0
"""
# def factor(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factor(n-1)
#
# n=int(input('Enter a number to facor: '))
# print(factor(n))


"""

Edureka solution
"""

num= int(input("Please enter the number of factors: "))
factor =1

if num<0:
    print("The factors must be  positive")
elif num ==0:
    print("Factor =1")
else:
    for i in range(1,num+1):
        factor *=i
print(factor)


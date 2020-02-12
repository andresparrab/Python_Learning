l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#slincing the list from index 2 to 9, not including the 9th item,and stride, jump over every other item,
print(l[2:9:2])



#Omitting indices
to_five = ['A', 'B', 'C', 'D', 'E']

print(to_five[3:])
# prints ['D', 'E']

print(to_five[:2])
# prints ['A', 'B']

print(to_five[::2])
# print ['A', 'C', 'E']


#print every odd number from start to end of the list
my_list = range(1, 11) # List of numbers 1 - 10

print(my_list[::2])

#reversin a list
letters = ['A', 'B', 'C', 'D', 'E']
print(letters[::-1])

#this reverse the list order and aisng it to the variable backwards
my_list = range(1, 11)

backwards = my_list[::-1]
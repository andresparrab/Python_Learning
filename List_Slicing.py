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

#more advance list
to_21 = range(1,21)
odds=to_21[::2]
middle_third=to_21[7:14]
print(sorted(to_21))
print(sorted(odds))
print(sorted(middle_third))


#The string in the editor is garbled in two ways:
# Our message is backwards.
#The letter we want is every other letter.

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
ungrable= garbled[::2]
message = ungrable[::-1]
print(message)
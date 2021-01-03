# example Line
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
# squares of the even numbers between 1 to 11
even_squares = [x ** 2 for x in range(1, 12) if x % 2 == 0]

print(even_squares)

# Another example of square comprehension
cubes_by_four = [x ** 3 for x in range(1, 11) if (x ** 3) % 4 == 0]
print(cubes_by_four)

# Dictionary comprehension
simple_dict = {
    "a": 1,
    "b": 2
}
# This take the value extracted from the dictionary.items() and return value**2 if the value is even
my_dict = {key: value ** 2 for key, value in simple_dict.items() if value%2==0}
print(my_dict)

# This take some_list and iterates the items and count how many times same value occur
# then apply the set function to get unique values and finally convert to list
some_list = ["a","b","c","b","d","m","n","n"]

duplicates = list(set(value for value in some_list if some_list.count(value)>1))
print(duplicates)
print(some_list)
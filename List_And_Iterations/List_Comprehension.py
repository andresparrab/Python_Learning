#example Line
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.
#squares of the even numbers between 1 to 11
even_squares = [x**2 for x in range(1,12) if x%2==0]

print(even_squares)

#Another example of square comprehention
cubes_by_four = [x**3 for x in range(1,11) if (x**3) % 4==0]
print(cubes_by_four)

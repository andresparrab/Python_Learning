my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "r+")

for item in my_list:
  f.write(str(item) + "\n")

f.close()

f = open("output.txt", "r+")
print(f.read())
f.close()


#another way to open file and close automaticly is like this:
with open('text.txt','w') as my_file:
  my_file.write('Succes!!!!')

#this if statment will check if the file is not close then close it.
if my_file.closed==False:
  my_file.close()

print(my_file.closed)
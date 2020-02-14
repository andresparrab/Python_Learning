import os
new_file = open("Edureka.txt", "r+")

for i in range(1,10):
    new_file.write("Welcome to python\n")

for i in range(1,10):
     print(new_file.readline(20))
#os.rename ("Edureka.txt", "new.txt")
new_file.close()
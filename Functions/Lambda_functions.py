my_list = range(16)
#print a list that filter out the number not evenly divided by 3, so print only the number evenly divided by 3
print(list(filter(lambda x: x % 3 == 0, my_list)))

languages = ["HTML", "JavaScript", "Python", "Ruby"]
#Print a list with the word 'Python' if is in the languages list, filter out everything else
print(list(filter(lambda word: word=='Python' ,languages)))

squares=[x**2 for x in range(1,11)]
# print a list with the squares numbers between 30 an 70
print(list(filter(lambda big_squares: 30<big_squares<71,squares)))

#Thi will print out another secret message after filter out the X:s in the phrase
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = list(filter(lambda x: x!='X',garbled))
print(''.join(message))
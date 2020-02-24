import matplotlib.pyplot as plt

x=range(5)
#plot several functions in the same graph calling plt.plot multiple times
#plt.plot(x, [x1 for x1 in x])
#plt.plot(x, [x1*x1 for x1 in x])
#plt.plot(x, [x1*x1*x1 for x1 in x])
#plt.show()

#plot several functions in the same graph calling plot one time
plt.plot(x, [x1 for x1 in x], x,[x1*x1 for x1 in x], x,[x1*x1*x1 for x1 in x], label='Jonatan')
#show a grid in the background
plt.grid(True)
#plt.show()

#to limit the axis where  is between 1 and 2.9 adn the y is (1.5 and 15)
#plt.axis([1,2.9,1.5,15])
plt.xlim(1,2.9)
plt.ylim(1.5,15)
#labes the axis
plt.xlabel('Gym Exersices')
plt.ylabel('Muscle grow')
#and add title
plt.title('Goku regiment training')
plt.legend()

plt.show()
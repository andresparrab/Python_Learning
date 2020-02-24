import matplotlib.pyplot as plt
import numpy as np


#simple plot creation with default x values n-1. there n is the lengh of the list
#plt.plot([1,2,3,4],[10,100])
#plt.show()

#another way to do do a aplot with x values
y_values = [1,2,3,4,10]
#print(i**2 for i in y_values)
plt.plot(y_values,[i**2 for i in y_values])
plt.show()

#you can also use Numpy to generate a list of items
x= np.arange(0,5,0.01)
plt.plot(x,[i**2 for i in x])
plt.show()
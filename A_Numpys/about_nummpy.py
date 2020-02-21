import numpy as np
#creates a array of type numpy with lists
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
#creates a np array from 0-99
b= np.arange(0,100)

#creates a np list with zeros. with dimention 3 rows and 5 columms
c= np.zeros((3,5))

#printing the ndimentionals arrays
print(a)
print(b)
print(c)


#Creates a np array with 8 zeroes in one line
x=np.zeros(8)
print(x)
#reshapes the  x array in 2x2 shapes
array3d= x.reshape((2,2,2))
print(array3d)
#ravels flattas the reshaped array
arrayflatten = array3d.ravel()
print(arrayflatten)
#creates a np array from 2-19
d=np.arange(2,20)
#from this array select the element in index 6
element = d[6]
print(d)
print(element)
import numpy as np
simpleaarray = np.arange(20)
print(simpleaarray)
arrySliced = slice(1,10,4)
print(simpleaarray[arrySliced])

#slicing multidimentional array
array2d = np.array([[1,2,3,],[3,4,5],[5,6,7]])
print(array2d)
print(array2d[0:3,1:3])
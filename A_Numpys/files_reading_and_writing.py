import numpy as np

arr1 = np.genfromtxt('newfile.csv',delimiter=';')
np.savetxt('newfile2.csv',arr1, delimiter=',')
newArray=np.loadtxt('newfile2.csv')
print(newArray)
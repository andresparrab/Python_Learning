import numpy as np

arr = np.loadtxt('filex.txt', dtype=int)
np.savetxt('newfile.txt',arr)
print(np.loadtxt('newfile.txt'))
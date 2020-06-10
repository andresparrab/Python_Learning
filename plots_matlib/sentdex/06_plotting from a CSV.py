from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

print(plt.style.available)
style.use('ggplot')


#unpacking the values into x and y:s
x,y = np.loadtxt('example.cvs',
                 unpack=True,
                 delimiter=',')
plt.plot(x,y)

plt.title('Epic chart')
plt.ylabel('Y yyy')
plt.xlabel('Xxxx')

plt.show()

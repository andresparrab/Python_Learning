import matplotlib.pyplot as plt
import numpy as np

y=np.random.rand(10,10)
print(y)
plt.hist(y,100)
plt.show()
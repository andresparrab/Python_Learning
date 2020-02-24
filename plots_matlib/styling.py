import matplotlib.pyplot as plt
import numpy as np

y= np.arange(1,40)
# The first function will be in red color and represented by --
# plt.plot(y, ('r''--'))
# the second function  will be in color magnetga represented by :
# plt.plot(y**2, ('m'':'))
# The third line will be in cyan color represented bu -.
# plt.plot(y**3, ('c''-.'))
# plt.show()
# this will style the function with red color and represented by triangle
plt.plot(y**2, ('r''^'))
plt.show()
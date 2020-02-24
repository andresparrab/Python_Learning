import matplotlib.pyplot as plt
import numpy as np

new_list =np.arange(5)
print(new_list)
plt.plot(new_list,[i*i for i in new_list], label='Jonatan')
plt.plot(new_list,[i*i*i for i in new_list], label='Cristian')
plt.plot(new_list,[i**4 for i in new_list], label='Andres')
plt.title('One Punch Man Mega Regiment')
plt.legend()
plt.xlabel('Days')
plt.ylabel('Muscle grow')
plt.ylim(0,20)
plt.grid(True)
#plt.show()
plt.savefig('My_first_plot.png')
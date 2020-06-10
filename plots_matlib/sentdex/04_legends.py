from matplotlib import pyplot as plt
from matplotlib import style

plt.grid(True, color='r')

x = [5,6,7,8]
y = [7,3,6,3]

x2 = [5,6,7,8]
y2 = [6,7,2,6]

print(len(x))
print(len(y))
print(plt.style.available)
style.use('ggplot')

plt.plot(x,y,'g',linewidth=5, label='line One')
plt.plot(x2,y2,'c',linewidth=10, label='Line Two')
plt.title('Epic chart')
plt.ylabel('Y yyy')
plt.xlabel('Xxxx')
plt.legend()
plt.show()
plt.grid(True, color='b')
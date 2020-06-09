from matplotlib import pyplot as plt
from matplotlib import style
x = [5,6,7,8]
y = [7,3,6,3]

x2 = [5,6,7,8]
y2 = [6,7,2,6]

print(len(x))
print(len(y))
print(plt.style.available)
style.use('ggplot')

plt.plot(x,y,'g',linewidth=5)
plt.plot(x2,y2)
plt.title('Epic chart')
plt.ylabel('Y yyy')
plt.xlabel('Xxxx')
plt.show()
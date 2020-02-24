import matplotlib.pyplot as plt

plt.figure(figsize=(3,3))
x=[40,20,5]
labels =['Jonatan', 'Cristian', 'Andres']
plt.pie(x,labels=labels)
plt.title('How much does the brothers eat')
plt.show()

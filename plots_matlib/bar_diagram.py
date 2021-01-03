import matplotlib.pyplot as plt


#Simple bar chart where the first  values are the midpoints of the bar and the second group of values are the height
#plt.bar([1.5, 2.6, 4.8], [40, 55, 85])
#plt.show()


#Dictionary bar graph

d= {'a':25, 'b':35, 'c':48}

for i, key in enumerate(d):
    plt.bar(i, d[key])
#xtick will replace the i in the graph with a labels
plt.xticks([0,1,2],['Jonatan', 'Cristian', 'Andres'])
plt.show()
print(i,key)

import pandas, numpy

#series = pandas.Series()
#print(series)

arr = numpy.array([10,20,30,40,50])
series =pandas.Series(arr)
print(series)

data_dict={'a':1,'b':2,'c':3,'d':400,'e':8,'f':9}
series_dict =pandas.Series(data_dict)
print(series_dict[2:5])
import numpy

a = numpy.array([[1, 2, 3], [4, 5, 6]])

b = numpy.array([[400], [800]])

newArray = numpy.append(a, b, axis = 1)

print(newArray)
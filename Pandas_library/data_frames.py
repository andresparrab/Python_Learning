import pandas

listx=[10,20,30,40]
table=pandas.DataFrame(listx)
print(table)

list_dict =[{'a':1,'b':34},{'a':45,'b':78},{'a':100,'b':3499}]
print(list_dict)
dict_table = pandas.DataFrame(list_dict,index=['jonatan','cristian','andres'])
print(dict_table)

data={'one': pandas.Series([1,2,3], index=['a','b','c']),
      'two': pandas.Series([1,2,3,4], index=['a','b','c','d'])
      }
data_table = pandas.DataFrame(data)
print(data_table)


#more advance and comprenhensiive table made out of two series
#much easier to read
subjects_scores1 = pandas.Series([40,45,69], index=['maths','chemmistry','physics'])
subjects_scores2 = pandas.Series([65,75,88,98], index=['maths','chemmistry','physics','c++'])

students_table = pandas.DataFrame({'Jim':subjects_scores1,'Andres':subjects_scores2})
print(students_table)

# adding a new columm in form of a new student
students_table['Jonatan'] = pandas.Series([12,45,99,34], index=['maths','chemmistry','physics','c++'])
print(students_table)
del(students_table['Jim'])
print(students_table)
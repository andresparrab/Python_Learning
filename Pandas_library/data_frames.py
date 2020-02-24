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
subjects_scores1 = pandas.Series([40,45,69], index=['maths','chemistry','physics'])
subjects_scores2 = pandas.Series([65,75,88,98], index=['maths','chemistry','physics','c++'])

students_table = pandas.DataFrame({'Jim':subjects_scores1,
                                   'Andres':subjects_scores2,
                                   'Pam':pandas.Series([23,45,76,342,54], index=['maths','chemistry','physics','c++', 'english'])
                                   })
print(students_table)

# adding a new columm in form of a new student
students_table['Jonatan'] = pandas.Series([12,45,99,34], index=['maths','chemistry','physics','c++'])
print(students_table)

# to delete a whole columm then use the del function like this
#del(students_table['Jim'])
#print(students_table)

#how to locate a row
print('\n\n')
print(students_table.loc['english'])

#how to add a whole new row append.
students_table=students_table.append(pandas.DataFrame([[90,56,32]], columns=['Jim','Andres','Jonatan']))
print(students_table)

#export the dataset to a csv
students_table.to_csv('students.csv')
students_table.to_excel(r'C:\Users\Gloria\PycharmProjects\adureka\Pandas_library\Students.xlsx')

#remove a row
students_table =students_table.drop('c++')
print(students_table)
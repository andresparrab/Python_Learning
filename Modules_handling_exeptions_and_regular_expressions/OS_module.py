import os

# print(os.name)

# print(os.environ)
# print(os.getlogin())
# print(os.getppid())

# print(os.getcwd())
# os.mkdir('Test')
# os.chdir('Test')
# print(os.getcwd())
# print(os.rmdir('Test'))

print(os.path.abspath('\Downloads\dnaAnalysys'))
# print(os.walk('C:\Downloads\dnaAnalysys'))
for i in os.walk('C:\Downloads\dnaAnalysys'):
    print(i)

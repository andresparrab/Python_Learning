import re

print(re.sub(r'[ad]','*','abcde abcedf abcdef'))
print(re.sub(r'abc','*','abcdef abcdef'))
print(re.sub(r'[abcd][1234]','*',' a1+b2+c3+d4+e5'))
print(re.sub(r'A.B','*', 'A2B AxB A£%B A$B'))
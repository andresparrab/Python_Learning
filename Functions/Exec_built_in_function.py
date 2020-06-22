exec("print('This works live eval')")

list_str = "[5,6,2,1,6]"
list_str = exec(list_str)

print(list_str)

exec("list_str2 = [5,6,23,4,5]")
print(list_str2)

exec("def test(): print('O sniiiiiiiippp snap !!!!')")
test()

exec("""
def test2(): 
    print('O sniiiiiiiippp snap 4!!!!')
""")
test2()
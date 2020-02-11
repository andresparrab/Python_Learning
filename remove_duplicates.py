def remove_duplicates(originaList):
    new_list=[]
    for number in originaList:
        if number in originaList:
            if number not in new_list:
                new_list.append(number)
    return new_list

print(remove_duplicates([1,2,2,3,4,5,5,2,7,7,7,7,1,1,1,9]))


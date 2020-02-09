def count(sequence,item):
    times=0
    for index in sequence:
        if index == item:
            times += 1
    return times

print(count([1,2,1,1],2))
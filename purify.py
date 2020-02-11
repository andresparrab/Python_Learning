def purify(numbers):
    even=[]
    for number in numbers:
        if number%2 ==0:
            even.append(number)
    return even


print(purify([1,2,3,4,5,6,7,8,9,0]))
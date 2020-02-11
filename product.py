def product(numbers):
    prod =1
    for number in numbers:
        prod = prod*number
    return prod

print(product([4,5,5]))
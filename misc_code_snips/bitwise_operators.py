#this function check if the 4  bit from the right is turn on or off. and return the word 'on' or 'off'
def check_bit4(input):
    num = input
    print(num)
    mask = 0b1000
    if num & mask > 0:
        return 'on'
    else:
        return 'off'

print(check_bit4(10))


#this  turn the third bit from the right on in variable a

a = 0b10111011
mask = 0b100
desired = a|mask

print(bin(desired))

#this flips the  bit from on till off an viseversa

a = 0b11101110
mask = 0b11111111
desired = a^mask
print(bin(desired))

#This function  flips the n:th bit from the right of the variable number
def flip_bit(number,n):
  mask = 0b1 << (n-1)
  result = number^mask
  return bin(result)

print(flip_bit(0b111,2))


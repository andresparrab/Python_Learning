for number in range(5):
  print(number, )

d = {
  "name": "Eric",
  "age": 26
}

for key in d:
  print(key, d[key], )

for letter in "Eric":
  print(letter, )  # note the comma!

my_dict = {
      'Name': 'Guido',
      'Age': '56',
      'BDFL': True
}

for key in my_dict:
      print(key, my_dict[key])
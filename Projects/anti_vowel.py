def anti_vowel(text):
  vowel='aeiouAEIOU'
# create a list that will hold the new characters
  result =[]
  # loop trough the text
  for char in text:
      # if the letter is not found in vowesl='aeiouAeiou' the add the character to the list result.
      if char not in vowel:
          result.append(char)
          # return the letter joined together as a string
  return ''.join(result)


print(anti_vowel('AndRes is the best in the world'))
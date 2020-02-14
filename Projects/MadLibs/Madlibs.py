'''
MadLibs by Andres Parra
Creates a Mad_libs story with the words that the user provides
'''

with open('story.txt','r') as file:
    Story = file.read()

#GLobal variables
#name = ''
adjectives = []
nouns = []
#verb = ''
key_words = {
    'animal': '',
    'food': '',
    'fruit': '',
    'superhero': '',
    'country': '',
    'dessert': '',
    'year': ''
}
print('Mad Libs is starting')
# Takes in the name of the main character
name = input('Please enter a name of the main character: ')
# Assign a verb to the variable verb
verb = input('Please enter a verb: ')
# appends 3 adjectives to the adjective list
for adj in range(3):
    adjectives.append(input('Please enter %d adjective:' % (adj+1)))
    print(adjectives[adj])
# appends 2 nouns to the nouns list
for noun in range(2):
    nouns.append(input('Please enter %d noun: ' % (noun+1)))
    print(nouns[noun])
# goes trough the dictionary one by one and assign the input
for item in key_words:
    key_words[item] = input('Please enter some %s: ' % (item))
    print(key_words[item])



print(key_words['superhero'])
print(adjectives[0])

print(Story % (name, adjectives[0], adjectives[1], key_words['animal'], key_words['food'], verb, nouns[0], key_words['fruit'], adjectives[2], name, key_words['superhero'], name, key_words['country'], name, key_words['dessert'], name, key_words['year'], nouns[1]))
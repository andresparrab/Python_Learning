#This function replace the word you want to cencor in the phrase to *
def censor(text,word):
    original=word
    for letter in word:
        word =word.replace(letter,'*')
    text=text.replace(original,word)
    return text


print(censor('this hack is wack, but i love to hack','hack'))


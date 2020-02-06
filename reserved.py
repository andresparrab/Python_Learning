def reverse(text):
    done = []
    index = len(text)
    for char in text:
        done.append(text[index-1])
        index -= 1
    return ''.join(done)
print(reverse("Hej Jag Heter Andres"))

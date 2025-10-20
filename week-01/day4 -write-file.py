words = ["virtus", "pietas", "gravitas"]

with open('latin_vocab.txt', 'w') as file:
    for word in words:
        file.write(word + '\n')
print("File created!")
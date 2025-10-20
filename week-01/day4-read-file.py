import os
print("Current directory:", os.getcwd())
print("Files here:", os.listdir())
with open('latin.txt', 'r') as file:
    content = file.read()
    print(content)
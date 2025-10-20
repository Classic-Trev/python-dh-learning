search_word = "partes"

with open('latin.txt') as file:
    for line in file:
        if search_word in line.lower():
            print(f"Found: {line.strip()})")
            
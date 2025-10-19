word = "virtus" #i could make this interactive using input()
vowels = "aeiou"

for letter in word.lower():
    if letter in vowels:
        print(f"Found vowel: {letter}")
    else:
        print(f"Found consonant: {letter}")
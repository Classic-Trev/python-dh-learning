def add_word(filename, word):
    with open(filename, 'a') as file: # 'a' means append, new not in lesson!
        file.write(word + '\n')
    print(f"Added: {word}")

def read_vocab(filename):
    try:
        with open(filename, 'r') as file:
            words = file.readlines()
            print(f"\n=== Vocabulary ({len(words)} words) ===")
            for word in words:
                print(word.strip())
    except FileNotFoundError:
        print("No vocabulary file found yet!")

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.readlines()
            return len(words)
    except FileNotFoundError:
        return 0
    
vocab_file = 'my_latin_vocab.txt'

add_word(vocab_file, "virtus")
add_word(vocab_file, "pietas")
add_word(vocab_file, "honor")

read_vocab(vocab_file)

total = count_words(vocab_file)
print(f"\nTotal words: {total}")
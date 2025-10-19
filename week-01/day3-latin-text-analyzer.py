# Sample Latin text (Caesar, Gallic Wars opening)
text = """
Gallia est omnis divisa in partes tres quarum unam incolunt Belgae
aliam Aquitani tertiam qui ipsorum lingua Celtae nostra Galli appellantur
"""

text_lower = text.lower()
words = text_lower.split()

print(f"Total words: {len(words)}")

for word in words:
    print(word)

word_count = {}. #creates a dictionary

for word in words:
    if word in word_count:
        word_count[word] += 1. # += means add to current value
    else:
        word_count[word] = 1 # because i defined word_count as a dictionary whatever i place in [] is a key, and what it is equal to is the value

print("\nWord frequencies:") ## \n creates a blank space
for word, count in word_count.items(): # word, count are also just iteration variables that could be named anything, mapped to key, value in dictionary
    print(f"{word}: {count}")

word_list = [] # creates a list
for word, count in word_count.items():
    word_list.append((count, word))

word_list.sort(reverse=True) #by default, sort orders numbers in ascending order; .sort(reverse=True) has it list in descending order!

print("\nTop 5 Most Common Words:")
for i in range(min(5, len(word_list))): # min() here is working with len() to ensure that this works if there are fewer than 5 words!
    count, word = word_list[i] # assigning variable names again keeping in mind reversed order!
    print(f"{i+1}. '{word}' appears {count} times")
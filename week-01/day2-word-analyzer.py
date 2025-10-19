def analyze_phrase(phrase):
        words = phrase.split()
        print(f"\n=== Analyzing Phrase: '{phrase}' ===")
        print(f"Word Count: {len(words)}")
        for word in words:
            analyze_word(word)
        return

def analyze_word(word): #only works for nominative singular nouns and adjectives
    def convert_to_vocative(word):
        word_lower = word.lower()
        if word.endswith('ius'):
            return word[:-2] + 'i'
        elif word.endswith('us'):
            return word[:-2] + 'e'
        else:
            return word

    def convert_to_genitive(word): 
        word_lower = word.lower()
        if word.endswith('us') or word.endswith('um'):
            return word[:-2] + 'i'
        elif word.endswith('a'):
            return word[:-1] + 'ae'
        elif word.endswith('u'):
            return word[:-1] + 'us'
        elif word.endswith('es'):
            return word[:-2] + 'i'
        else:
            return "Irregular 3rd Declension" #future project

    def convert_to_dative(word):
        word_lower = word.lower()
        if word.endswith('us') or word.endswith('um'):
            return word[:-2] +'o'
        elif word.endswith('a'):
            return word[:-1] + 'ae'
        elif word.endswith('u'):
            return word
        elif word.endswith('es'):
            return word[:-1] + 'i'
        else:
            return "Irregular 3rd Declension"
        
    def convert_to_accusative(word):
        word_lower = word.lower()
        if word.endswith('us') or word.endswith('um'):
            return word[:-2] +'um'
        elif word.endswith('a'):
            return word[:-1] + 'am'
        elif word.endswith('u'):
            return word
        elif word.endswith('es'):
            return word
        else:
            return "Irregular 3rd Declension"
        
    def convert_to_ablative(word):
        word_lower = word.lower()
        if word.endswith('us') or word.endswith('um'):
            return word[:-2] +'o'
        elif word.endswith('a'):
            return word
        elif word.endswith('u'):
            return word
        elif word.endswith('es'):
            return word[:-1]
        else:
            return "Irregular 3rd Declension"

    def guess_declension(word):
        word_lower = word.lower()
        if word_lower.endswith('a'):
            return "Probably 1st declension"
        elif word_lower.endswith('us') or word_lower.endswith('um'):
            return "Probably 2nd declension"
        elif word_lower.endswith('u'):
            return "probably 4th declension" #unable to account for masc/fem 4th decl. at this time. will try to revisit.
        elif word_lower.endswith('es'):
            return "probably 5th declension"
        else:
            return "probably 3rd declension"
            
        
    def check_patterns(word):
        word_lower = word.lower()
        patterns = [] #look into this!

        if 'll' in word_lower or 'nn' in word_lower or 'm' in word_lower:
            patterns.append("Contains geminate consonants")

        if 'ae' in word_lower:
            patterns.append("Contains 'ae' diphthong")
        if 'oe' in word_lower:
            patterns.append("Contains 'oe' diphthong")
        if 'ei' in word_lower:
            patterns.append("Contains 'ei' diphthong")
        if 'eu' in word_lower:
            patterns.append("Contains 'eu' diphthong")
        if 'ui' in word_lower:
            patterns.append("Contains 'ui' diphthong")
        return patterns
    
    def count_syllables_approx(word):
        vowels = "aeiou"
        word_lower = word.lower()
        count = 0
        previous_was_vowel = False

        for letter in word_lower: ###REVIEW PARAGRAPH
            is_vowel = letter in vowels
            if is_vowel and not previous_was_vowel:
                count += 1
            previous_was_vowel = is_vowel
        return count if count > 0 else 1

    #basic info
    declension = guess_declension(word)
    patterns = check_patterns(word)
    syllables = count_syllables_approx(word)
    length = len(word)
    upper_version = word.upper()
    lower_version = word.lower()
    vocative = convert_to_vocative(word)
    genitive = convert_to_genitive(word)
    dative = convert_to_dative(word)
    accusative = convert_to_accusative(word)
    ablative = convert_to_ablative(word)

    #check if it' long or short
    if length <= 5:
        size = "short"
    elif length <= 8:
        size = "medium"
    else:
        size = "long"
    
    #count vowels
    vowels = 0
    for letter in word.lower(): #not familiar with for yet but I'm told it has to do with loops!
        if letter in 'aeiou':
            vowels += 1

    print(f"\n=== Analysis of '{word}' ===") #\n is new. Noted!
    print(f"Declension: {declension}")
    print(f"Length: {length} letters ({size} word)")
    print(f"Uppercase: {upper_version}")
    print(f"Lowercase: {lower_version}")
    print(f"Vowels: {vowels}")
    print(f"Consonants: {length - vowels}")
    print(f"Patterns: {', '.join(patterns) if patterns else 'None'}") ###REVIEW
    print(f"Syllables: {syllables}")
    print(f"Nominative: {word}")
    print(f"Genitive: {genitive}")
    print(f"Dative: {dative}")
    print(f"Accusative: {accusative}")
    print(f"Ablative: {ablative}")
    print(f"Vocative: {vocative}")
    
    return





phrase = (input("Enter Nominative Latin Noun or Noun Phrase:" ))
analyze_phrase(phrase)
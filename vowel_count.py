# Vowel count
# 7 kyu

# Return the number (count) of vowels in the given string.

def get_count(sentence):
    num_vowels = 0
    for char in sentence:
        if char in "aeiou":
            num_vowels += 1
    return num_vowels
    pass

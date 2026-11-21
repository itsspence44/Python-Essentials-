word_without_vowels = ""

user_word = input("Enter a word: ")

for letter in user_word:
    if letter.lower() not in "aeiou":
        word_without_vowels += letter

print(word_without_vowels)

import string

# Input a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words, remove punctuation and convert to lowercase
words = sentence.split()
cleaned_words = [word.strip(string.punctuation).lower() for word in words]

# Find the duplicate word
duplicate_word = None
for word in cleaned_words:
    if cleaned_words.count(word) == 2:
        duplicate_word = word
        break

# Output the result 
if duplicate_word:
    print(f"Duplicate word: {duplicate_word}")
else:
    print("No duplicate word found.")
     
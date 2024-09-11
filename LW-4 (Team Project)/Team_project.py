# Made by Natan Nedaikhlib

# Initial text for processing 
text = "Scientists have stated that new research will help understand how cosmic factors influence climate change on Earth. Similar research is important for developing strategies to counteract climate changes."

# 1. Convert the entire text to lowercase
lower_text = text.lower()
print("Text in lowercase: ", lower_text)

# 2. Split the text into words
words = lower_text.split()
print("Words in the text", words)

# 3. Remove punctuation from words
import string
clean_words = [word.strip(string.punctuation) for word in words]
print("Words without punctuation:", clean_words)

# 4. Count the number of words in the text
word_count = len(clean_words)
print("Number of words in the text: ", word_count)


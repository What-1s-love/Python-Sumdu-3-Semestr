def count_vowels_and_consonants(text):
    # Define the set of vowels
    vowels_set = {'a', 'e', 'i', 'o', 'u', 'y'}
    
    # Create a set from the text containing only letters
    letters_set = set(char.lower() for char in text if char.isalpha())
    
    # Since we cannot count duplicates in a set, convert the set to a list
    letters_list = [char.lower() for char in text if char.isalpha()]
    
    # Count vowels and consonants
    vowels_count = sum(1 for char in letters_list if char in vowels_set)
    consonants_count = sum(1 for char in letters_list if char not in vowels_set)
    
    # Determine which count is higher
    if vowels_count > consonants_count:
        result = "There are more vowels."
    elif consonants_count > vowels_count:
        result = "There are more consonants."
    else:
        result = "The number of vowels and consonants is equal."
    
    # Convert the result list back into a set for display
    result_set = set(letters_list)
    print("Set of letters in the text:")
    print(result_set)
    print(result)

# Input text from the user
text = input("Enter text containing digits and Latin letters: ")
count_vowels_and_consonants(text)

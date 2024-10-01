def every_third_element(lst):
    return lst[2::3]

# Input the list from the user
user_input = input("Enter the list elements separated by spaces: ")
lst = user_input.strip().split()

# Form a new list containing every third element
new_list = every_third_element(lst)

# Print the new list
print("New list containing every third element:")
print(' '.join(new_list))

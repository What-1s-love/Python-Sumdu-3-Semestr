def remove_element(lst, value):
    return [item for item in lst if item != value]

# Input the list from the user
user_input = input("Enter the list elements separated by spaces: ")
lst = user_input.strip().split()

# Input the value to remove
value_to_remove = input("Enter the value to remove from the list: ")

# Remove the specified value from the list
updated_list = remove_element(lst, value_to_remove)

# Print the updated list
print("Updated list:")
print(updated_list)



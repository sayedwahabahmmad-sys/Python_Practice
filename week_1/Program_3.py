# Program to CREATE, JOIN, and EXTRACT substrings in a string

# Step 1: Create two strings
string1 = "Python"
string2 = "Programming"

# Step 2: Concatenate the strings with a space
concatenated_string = string1 + " " + string2

# Step 3: Print the concatenated string
print("Concatenated String:", concatenated_string)  # Output: Python Programming

# Step 4: Extract the first 6 characters ("Python")
substring1 = concatenated_string[0:6]
print("Substring (first 6 characters):", substring1)

# Step 5: Extract substring from index 7 to the end ("Programming")
substring2 = concatenated_string[7:]
print("Substring from index 7 to end:", substring2)

# Step 6: Access a specific character at index 1 ("y")
specific_character = concatenated_string[1]
print("Specific character at index 1:", specific_character)

# Step 7: Extract substring using negative indexing ("Programming")
# "Programming" is the last 11 characters in "Python Programming"
substring3 = concatenated_string[-11:]
print("Substring using negative indexing:", substring3)

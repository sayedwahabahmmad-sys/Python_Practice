# Write a program using filter() to filter only even numbers from a list

# Original list of numbers
numbers = [1, 2, 3, 4, 5]

# Using filter() to select only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Printing the filtered list
print("Even numbers:", even_numbers)

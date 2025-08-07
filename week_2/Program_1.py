# Create a tuple
my_tuple = (10, 20, 30)

# 1) Add items (tuples are immutable, so we create a new tuple)
my_tuple += (40,)  # Add 40 to the tuple
print("After adding an item:", my_tuple)

# 2) Get the length of the tuple
tuple_length = len(my_tuple)
print("Length of tuple:", tuple_length)

# 3) Check for item in tuple
item_check = 20 in my_tuple
print("Is 20 in the tuple?", item_check)

# 4) Access items
first_item = my_tuple[0]  # Access first item
print("First item in tuple:", first_item)

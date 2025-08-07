# Create a dictionary
my_dict = {
    "name": "Sayed Wahab Ahmmad",
    "age": 21,
    "city": "Dubai"
}

# 1) Print the dictionary items
print("Dictionary items:", my_dict.items())

# 2) Access items
name = my_dict["name"]
print("Accessed name:", name)

# 3) Use get()
age = my_dict.get("age")
print("Accessed age using get():", age)

# 4) Change values
my_dict["city"] = "Los Angeles"  # Change city
print("After changing city:", my_dict)

# 5) Use len()
dict_length = len(my_dict)
print("Length of dictionary:", dict_length)

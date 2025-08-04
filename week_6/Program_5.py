# Write a program to double a given number and add two numbers using lambda()

# Lambda to double a number
double = lambda x: x * 2

# Lambda to add two numbers
add = lambda a, b: a + b

# Example usage
number = int(input("Enter a number to double: "))
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

print("Double of", number, "is:", double(number))
print("Sum of", num1, "and", num2, "is:", add(num1, num2))

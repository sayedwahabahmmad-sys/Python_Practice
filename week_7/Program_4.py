print("Program starts")

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    
    result = x / y
    print("Result:", result)

except ValueError:
    print("Please enter valid integers only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

print("Program ends")

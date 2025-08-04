#Demonstrate a Python code to print "try", "except", and "finally" block statements

try:
    print("Block = Try.")
    x = 1 / 0  # This will raise a ZeroDivisionError

except ZeroDivisionError:
    print("Block = Except.")

finally:
    print("Block = Finally.")

# try - This block runs first. It contains code that might cause an error.
# except - This block runs if an error occurs in the try block.
# finally - This block always runs, regardless of whether an error occurred or not.

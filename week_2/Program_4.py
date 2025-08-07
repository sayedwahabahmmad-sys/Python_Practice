# Formula: C/5 = (F - 32)/9

def temperature_conversion():
    temp = float(input("Enter temperature: "))
    unit = input("Is this temperature in Celsius (C) or Fahrenheit (F)? ").strip().upper()

    if unit == 'C':
        fahrenheit = (temp * 9/5) + 32
        print(f"{temp}°C is {fahrenheit:.2f}°F")
    elif unit == 'F':
        celsius = (temp - 32) * 5/9
        print(f"{temp}°F is {celsius:.2f}°C")
    else:
        print("Invalid unit. Please enter C or F.")

if __name__ == "__main__":
    temperature_conversion()

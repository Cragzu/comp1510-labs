start = input("Do you want to convert from [C]elsius or from [F]ahrenheit? ")

if start == "C" or start == "c":
    celsius = float(input("Enter a temperature in Celsius: "))
    fahrenheit = (celsius*1.8) + 32.0
    print(celsius, "degrees Celsius is", fahrenheit, "degrees Fahrenheit.")

elif start == "F" or start == "f":
    fahrenheit = float(input("Enter a temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    print(fahrenheit, "degrees Fahrenheit is", celsius, "degrees Celsius.")

else:
    print("That wasn't a valid response.")
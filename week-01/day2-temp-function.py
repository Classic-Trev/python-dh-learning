def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
print(f"25°C = {celsius_to_fahrenheit(25)}°F")
print(f"77°F = {fahrenheit_to_celsius(77)}°C")
#maybe make it better?

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
temp = float(input("What is the temperature?" ))
kind = input("Metric or Imperial?" )
if kind == "Metric":
    print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")
else:
    print(f"{temp}°F = {fahrenheit_to_celsius(temp)}°C")
#HOT DOG! (i swear im not old)
#Needed a little help from Claude to figure out what was wrong;
#gotta remember to convert number inputs from strings to int/float before math!

##realization: could conditions with elif for fahrenheit and else could result in error
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius
temp = float(input("What is the temperature?" ))
kind = input("Metric or Imperial?" )
if kind == "Metric":
    print(f"{temp}°C = {celsius_to_fahrenheit(temp)}°F")
elif kind == "Imperial":
    print(f"{temp}°F = {fahrenheit_to_celsius(temp)}°C")
else:
    print("error")
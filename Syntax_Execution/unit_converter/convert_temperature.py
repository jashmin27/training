
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

celsius = float(input("Enter temperature in Celsius: "))
print(f"{celsius}C = {celsius_to_fahrenheit(celsius):.2f}F")
print(f"{celsius}C = {celsius_to_kelvin(celsius):.2f}K")

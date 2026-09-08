
def length_menu():
    km = float(input("Enter km: "))
    print(f"{km} km = {km * 0.621371:.2f} miles\n")

def weight_menu():
    kg = float(input("Enter kg: "))
    print(f"{kg} kg = {kg * 2.20462:.2f} lb\n")

def temperature_menu():
    c = float(input("Enter Celsius: "))
    print(f"{c}C = {(c * 9/5) + 32:.2f}F\n")

menu_options = {
    "1": ("Length (km to miles)", length_menu),
    "2": ("Weight (kg to lb)", weight_menu),
    "3": ("Temperature (C to F)", temperature_menu),
}

while True:
    print("---- Unit Converter ----")
    for key, (label, _) in menu_options.items():
        print(f"{key}. {label}")
    print("4. Exit")

    choice = input("Choose an option: ")
    if choice == "4":
        print("Goodbye!")
        break
    elif choice in menu_options:
        menu_options[choice][1]()
    else:
        print("Invalid choice, try again.\n")

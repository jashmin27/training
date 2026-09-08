
KG_TO_LB = 2.20462
KG_TO_GRAM = 1000

kg = float(input("Enter weight in kilograms: "))
pounds = kg * KG_TO_LB
grams = kg * KG_TO_GRAM

print(f"{kg} kg = {pounds:.2f} lb")
print(f"{kg} kg = {grams:.0f} g")

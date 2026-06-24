MAX_WEIGHT = 20.0

A = float(input("What is your package weight (kg)? "))

if A > MAX_WEIGHT:
    print("Your package is overweight.")
else:
    print("Your package is not overweight.")
x = float(input("Input the air temperature (in Kelvin): "))
y = float(input("Input the steam temperature (in Kelvin): "))

ans = 1 - x / y

if y < 373:
    print("Efficiency = 0")
else:
    print(f"Efficiency = {ans}")
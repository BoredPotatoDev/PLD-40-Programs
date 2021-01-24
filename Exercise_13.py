print("Enter an integer for X and Y to get the Harmonic and Arithmetic mean")
x = int(input("Enter x: "))
y = int(input("Enter y: "))

h = 2/(1/x + 1/y)
a = (x+y)/2

print(f"\nArithmetic mean: {a}")
print(f"Harmonic mean: {h}")
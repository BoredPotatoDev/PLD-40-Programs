from fractions import Fraction
print("Given 3x^2 - 8x + 4")
x = str(input("Assign a value for X: "))
y = Fraction(x)

ans = 3*(y**2) - 8*(y) + 4

print(f"At 2 = {x} the value is {ans}")
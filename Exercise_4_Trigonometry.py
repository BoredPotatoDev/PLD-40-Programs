import math
value = float(input("Input you radian: "))

x = math.sin(value)
y = math.cos(value)
ans = x**2 + y**2

print(f"sine: {x} cosine: {y} sum: {ans}")
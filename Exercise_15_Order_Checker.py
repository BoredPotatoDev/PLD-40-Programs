b = 5
n = 3
w = 1

x = int(input("Number of bolts: "))
y = int(input("Number of nuts: "))
z = int(input("Number of washer: "))

if x > y:
    print("Check The Order!")
else:
    print("Order is OK!")

ans = (x*b)+(y*n)+(z*w)
print(f"Total Cost: {ans} cents")
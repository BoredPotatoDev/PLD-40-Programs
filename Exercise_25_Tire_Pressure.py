x = int(input("Input right front pressure: "))
y = int(input("Input left front pressure: "))
a = int(input("Input right back pressure: "))
b = int(input("Input left back pressure: "))

if x == y and a == b:
    print("Inflation is OK!")
else:
    print("Inflation is BAD!")
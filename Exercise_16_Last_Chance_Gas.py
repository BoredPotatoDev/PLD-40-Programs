x = int(input("Tank Capacity (in gallons): "))
y = int(input("Gage reading: "))
z = int(input("Miles per gallon: "))

ans = (x*(y/100))*z

if ans < 200:
    print("Get Gas!")
else:
    print("Safe to Proceed")
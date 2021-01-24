x = int(input("Input the number of items heated: "))
y = float(input("Input the reccomended heating time (in seconds): "))

if x == 1:
    print(y)
if x == 2:
    y = y + (y * .5)
    print(y)
if x == 3:
    y *= 2
    print(y)
if x > 3:
    print("More than 3 items are not recommended")
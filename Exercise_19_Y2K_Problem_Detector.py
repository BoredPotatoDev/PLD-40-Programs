x = int(input("Year of Birth: "))
y = int(input("Current Year: "))

if x > y:
    ans = (100 + y) - x
    print(ans)
if x < y:
    ans = y - x
    print(ans)
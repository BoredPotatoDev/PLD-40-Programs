x = str(input("Enter the first word: "))
y = str(input("Enter the second word: "))

add = len(x) + len(y)
dots = 30 - add

if dots == 0:
    print(f"{x}{y}")
else:
    print(x, end="")
    for i in range (1, dots+1):
        print(".", end="")
    print(y, end="")
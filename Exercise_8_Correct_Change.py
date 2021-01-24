x = int(input("Input your change due (in cents): "))

print("Your change is: ", end= "")
if x == 0:
    print("no change")
if x//100 >= 1:
    if x//100 == 1:
        print(f"{x//100} dollar", end= " ")
        x = x % 100
    elif x//100 > 1:
        print(f"{x//100} dollars", end= " ")
        x = x % 100
if x//25 >= 1:
    if x//25 == 1:
        print(f"{x//25} quarter", end= " ")
        x = x % 25
    elif x//25 > 1:
        print(f"{x//25} quarters", end= " ")
        x = x % 25
if x//10 >= 1:
    if x//10 == 1:
        print(f"{x//10} dime", end= " ")
        x = x % 10
    elif x//10 > 1:
        print(f"{x//10} dimes", end= " ")
        x = x % 10
if x//5 >= 1:
    if x//5 == 1:
        print(f"{x//5} nickel", end= " ")
        x = x % 5
    elif x//5 > 1:
        print(f"{x//5} nickels", end= " ")
        x = x % 5
if x//1 >= 1:
    if x//1 == 1:
        print(f"{x//1} penny", end= " ")
    elif x//1 > 1:
        print(f"{x//1} pennies", end= " ")
x = int(input("Input the balance in checking account (in dollars): "))
y = int(input("Input the balance in saving account (in dollars): "))

if x >= 1000 or y >= 1500:
    print("No service charge")
else:
    print("Service charge is $0.15 per check")
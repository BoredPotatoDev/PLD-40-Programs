x = int(input("Enter amount of purchases (in cents): "))

if x < 1000:
    print(f"Discounted price: {x}")
else:
    x = x - (x * .10)
    print(f"Discounted price: {x}")
x = float(input("Enter the cost per killowatt-hour in cents: "))
y = float(input("Enter the killowatt-hours used per year: "))

ans = x*y/100
ans = round(ans,2)
print(f"Annual cost: {ans} dollars")
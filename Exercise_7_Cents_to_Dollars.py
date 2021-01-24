x = input("Input the cents: ")

a = x[:-2]
b = x[-2:]

if int(x) > 99:
    print(f"{a} dollars and {b} cents")
else: 
    print(f"0 dollars and {b} cents")
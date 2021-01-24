x = input("Enter the Item: ")
y = float(input("Enter the Price (in cents): "))
z = int(input("Overnight delivery? (0 = no, 1 = yes): "))

if y > 1000:
    s = 3.00
if y < 1000:
    s = 2.00
    
if z == 1:
    s += 5.00

ans = y+s

print(f"Invoice: \n{x}: {y} \nshipping: {s} \ntotal: {ans}")
x = int(input("How many integers will be added: "))
a = []

for i in range (1, x+1):
    y = int(input("Enter and integer: "))
    a.append(y)

print(f"The sum is {sum(a)}")
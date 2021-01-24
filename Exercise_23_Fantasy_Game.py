print("Welcome to Yertle's Quest!")
x = input("Enter the name of your character: ")
s = int(input("Enter stength (1-10): "))
h = int(input("Enter health (1-10): "))
l = int(input("Enter luck (1-10): "))

total = s+h+l

if total > 15:
    print(f"You have given your character too many points! Default Values have been assigned: \n{x}, Strength: 5, Health: 5, Luck: 5")
else:
    print(f"Welcome adveturer {x}!\nStrength: {s}, Health: {h}, Luck: {l}")
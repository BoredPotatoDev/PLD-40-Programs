xa = float(input("Price per pound package A: "))
ya = float(input("Percent lean package A: "))

xb = float(input("Price per pound package B: "))
yb = float(input("Percent lean package B: "))

ansA = round(xa / ya * 100,2)
ansB = round(xb / yb * 100,2)

print(f"Package A cost per pound of lean: {ansA}")
print(f"Package B cost per pound of lean: {ansB}")

if ansA > ansB:
    print("Package B is best value")
if ansA < ansB:
    print("Package A is best value")
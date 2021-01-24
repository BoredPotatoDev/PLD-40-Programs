goodPressure = True

x = int(input("Input right front tire pressure: "))
if x not in range (35,45):
    goodPressure = False
    if goodPressure == False:
        print("Warning: pressure out of range")

y = int(input("Input left front tire pressure: "))
if y not in range (35,45):
    goodPressure = False
    if goodPressure == False:
        print("Warning: pressure out of range")

ax = int(input("Input right rear tire pressure: "))
if ax not in range (35,45):
    goodPressure = False
    if goodPressure == False:
        print("Warning: pressure out of range")

ay = int(input("Input left rear tire pressure: "))
if ay not in range (35,45):
    goodPressure = False
    if goodPressure == False:
        print("Warning: pressure out of range")

if goodPressure == True:
    if y in range (x-3, x+4) and ay in range (ax-3, ax+4):
        print("Inflation is GOOD")
    else:
        print("Inflation is BAD")
else: 
    print("Inflaition is BAD")
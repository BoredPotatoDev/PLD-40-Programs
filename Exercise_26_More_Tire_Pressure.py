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

if goodPressure == False:
    print("Inflation is BAD")
if goodPressure == True:
    print("Inflation is OK")
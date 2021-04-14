print("Welcome in TIP CALCULATOR")
total = float(input("Total Bill is $ "))
people = int(input("How many people to split? "))
percentage = float(input("What percentage tip? % "))
result = (total + (total*(percentage/100)))/people
print(f"Each person should pay: {result} $")



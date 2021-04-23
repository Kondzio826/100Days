from replit import clear
def add(a,b):
    return a + b

def minus(a,b):
    return a - b

def divide(a,b):
    return a / b

def multiply(a,b):
    return a * b

symbols={"+": add,
"-" : minus,
"*" : multiply,
"/" : divide
}

choice = ""

num1 = float(input("Give me first number:\n"))
while choice != "no":
    for i in symbols:
        print(f"\n{i}")
    symbol = input("Which symbol choose?\n")
    num2 = float(input("Give me second number:\n"))

    result = symbols[symbol]
    print(f"Result is {result(num1,num2)}")
    choice = input("You want continue? yes/no \n")
    num1 = result(num1,num2)
    if choice == "yes":
        clear()
        print(f"Number one is {num1}")

print(f"Final Result is {num1}")

# simple arithmetic operations
x = input('Please insert x variable: ')
y = input('Please insert y variable: ')
x = int(x)
y = int(y)
operation = input('Please insert math operation: ')

if operation == "+":
    calc = x + y
    print(calc)
elif operation == "-":
    calc = x - y
    print(calc)
elif operation == "*":
    calc = x * y
    print(calc)
elif operation == "/":
    if y == 0:
        print("Div by Zero")
    calc = x * y
    print(calc)
elif operation == "//":
    calc = x // y
    print(calc)
else:
    print("operation is not valid")

operator = input("Enter you operation(+ - * /) = ")
number1 = float(input("Enter you first value = "))
number2 = float(input("Enter you second value = "))
if operator == "+":
    result = number1 + number2
    print(result)
elif operator == "-":
    result = number1 - number2
    print(result)
elif operator == "*":
    result = number1 * number2
    print(result)
elif operator == "/":
    result = number1 / number2
    print(result)
else:
    print("Your operator does not exsist")

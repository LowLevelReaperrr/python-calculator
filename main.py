#Python Calculator!
print("Hello and welcome to my simple python calculator, it can perform functions such as(+, -, /, *)\n")
print("As well as the modulus operator and floor division!\n")

#Setting Operator Functions
def op_function(num1, num2, op):
    if op == "+":
        print("The Answer is" + num1 + num2)
    elif op == "-":
        print("The Answer is" + num1 - num2)
    elif op == "*":
        print("The Answer is" + num1 * num2)
    elif op == "/":
        print("The Answer is" + num1 / num2)
    elif op == "//":
        print("The Answer is" + num1 // num2)
    elif op == "**":
        print("The Answer is" + num1 ** num2)
    elif op == "%":
        print("The Answer is" + num1 % num2)
    else:
        print("INVALID OPERATOR! :/ TRY AGAIN!")

while True:
    num1 = input("Enter a number: ")
    op = input("Enter an operator: ")
    num2 = input("Enter another number: ")
    op_function(num1, num2, op)

    option = input("Keep calculating? (Yes/No): ")
    if option.lower() == "no":
        break

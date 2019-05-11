num1 = float(input("Enter first Number: "))
opt = input("Enter a Operator: ")
num2 = float(input("Enter second Number: "))

if opt == "+":
    print(num1 + num2)
    
elif opt =="-":
    print(num1 - num2)

elif opt == "*":
    print(num1 * num2)
    
elif opt == "/":
    print(num1 / num2)
else:
    print("Invalid Operator")
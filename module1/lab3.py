# Simple Calculator

print("=" * 30)
print("       CALCULATOR")
print("=" * 30)

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero"

else:
    result = "Invalid operator"

print("-" * 30)
print("Result:", result)
print("=" * 30)

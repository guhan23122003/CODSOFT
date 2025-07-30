num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose an operation:")
print("1. Add (+)")
print("2. Subtract (-)")
print("3. Multiply (*)")
print("4. Divide (/)")

operation = input("Enter any operation (1/2/3/4): ")
result = None

if operation == '1':
    result = num1 + num2
    op = '+'
elif operation == '2':
    result = num1 - num2
    op = '-'
elif operation == '3':
    result = num1 * num2
    op = '*'
elif operation == '4':
    if num2 != 0:
        result = num1 / num2
        op = '/'
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation.")

if result is not None:
    print(f"{num1} {op} {num2} = {result}")

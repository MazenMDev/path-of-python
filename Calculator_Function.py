def calculator():
    print("Welcome to the calculator program!")
    print("Please enter two numbers:")

    # Input two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform calculations
    sum_result = num1 + num2
    diff_result = num1 - num2
    prod_result = num1 * num2
    div_result = num1 / num2 if num2 != 0 else "undefined (division by zero)"

    # Display results
    print(f"Sum: {sum_result}")
    print(f"Difference: {diff_result}")
    print(f"Product: {prod_result}")
    print(f"Quotient: {div_result}")

calculator()

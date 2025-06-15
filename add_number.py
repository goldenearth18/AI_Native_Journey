# Get input for the first number
num1_str = input("Enter the first number: ")

# Get input for the second number
num2_str = input("Enter the second number: ")

try:
    # Convert inputs to numbers (integers for simplicity, can use float() for decimals)
    num1 = int(num1_str)
    num2 = int(num2_str)

    # Calculate the sum
    sum_result = num1 + num2

    # Print the result
    print(f"The sum of {num1} and {num2} is: {sum_result}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
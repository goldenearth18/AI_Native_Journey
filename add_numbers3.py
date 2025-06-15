# --- Python Script to Add Three Numbers ---

def add_three_numbers_script():
  """
  This function prompts the user to enter three numbers,
  converts them to floating-point numbers (to allow for decimals),
  calculates their sum, and then prints the result.
  It also includes basic error handling for non-numeric input.
  """

  print("Let's add three numbers together!")

  try:
    # Prompt for the first number and convert it to a float
    num1_str = input("Enter the first number: ")
    num1 = float(num1_str) # Use float() to handle whole numbers or decimals

    # Prompt for the second number and convert it to a float
    num2_str = input("Enter the second number: ")
    num2 = float(num2_str)

    # Prompt for the third number and convert it to a float
    num3_str = input("Enter the third number: ")
    num3 = float(num3_str)

    # Calculate the sum of the three numbers
    total_sum = num1 + num2 + num3

    # Display the result to the user
    print(f"\nThe sum of {num1}, {num2}, and {num3} is: {total_sum}")

  except ValueError:
    # If the user enters something that can't be converted to a number,
    # a ValueError occurs. This block catches it and prints an error message.
    print("\nOops! That wasn't a valid number. Please enter only numeric values.")

# This line ensures the function runs only when the script is executed directly.
if __name__ == "__main__":
  add_three_numbers_script()
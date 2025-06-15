
def welcome_message(name):
  """
  Generates a personalized welcome message.

  Args:
    name: The name of the person to welcome (string).

  Returns:
    A personalized welcome message (string).
  """
  return f"Hello, {name}! Welcome to the world of Python!"

# Get the user's name as input
user_name = input("Please enter your name: ")

# Generate and print the welcome message
message = welcome_message(user_name)
print(message)
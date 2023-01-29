# Get user information
print("Please enter your personal information.")

# Get user name
name = input("What is your name? ")

# Get user age
age = input("What is your age? ")

# Check that age is numeric
while not age.isdigit():
    print("Please enter a valid age.")
    age = input("What is your age? ")

# Get user address
address = input("What is your address? ")

# Get user email
email = input("What is your email address? ")

# Check that email contains '@' and '.'
while '@' not in email or '.' not in email:
    print("Please enter a valid email address.")
    email = input("What is your email address? ")

# Print a summary
print("\nSummary of your information")
print("Name:", name)
print("Age:", age)
print("Address:", address)
print("Email:", email)

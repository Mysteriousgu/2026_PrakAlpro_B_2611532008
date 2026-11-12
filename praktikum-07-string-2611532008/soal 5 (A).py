# Name: Muhammad Rafi Firdaus
# NIM: 2611532008
# Question 5 (A)
username = input("Username: ")

if not username[0].isalpha():
    print("Invalid: Must start with a letter")
elif len(username) < 5:
    print("Invalid: at least 5 characters")
elif not username.isalnum():
    print("Invalid: Letters and digits only")
else:
    print("Valid")
# Check the rules in a safe order and print the first rule that fails.
# Messages:
#   "Invalid: at least 5 characters"
#   "Invalid: letters and digits only"
#   "Invalid: must start with a letter"
#   "Valid"
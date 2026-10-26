# Case Study 29: Password Policy Validation Engine
password = input("Enter a sample password to validate: ")
errors = []

if len(password) < 8:
    errors.append("Must contain at least 8 characters.")
if not any(ch.islower() for ch in password):
    errors.append("Must contain a lowercase letter.")
if not any(ch.isupper() for ch in password):
    errors.append("Must contain an uppercase letter.")
if not any(ch.isdigit() for ch in password):
    errors.append("Must contain a digit.")
if not any(not ch.isalnum() for ch in password):
    errors.append("Must contain a special character.")
if "password" in password.lower():
    errors.append("Must not contain the word 'password'.")

if errors:
    print("Password does not meet the sample policy:")
    for error in errors:
        print("-", error)
else:
    print("Password meets the sample policy.")
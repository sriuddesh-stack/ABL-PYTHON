# Case Study 29: Password Policy Validation Engine
# Use a made-up sample password for this classroom exercise.
password = input("Enter a sample password to validate: ")
errors = []

has_lower = False
has_upper = False
has_digit = False
has_special = False

for ch in password:
    if ch >= "a" and ch <= "z":
        has_lower = True
    elif ch >= "A" and ch <= "Z":
        has_upper = True
    elif ch >= "0" and ch <= "9":
        has_digit = True
    else:
        has_special = True

if len(password) < 8:
    errors.append("Must contain at least 8 characters.")
if not has_lower:
    errors.append("Must contain a lowercase letter.")
if not has_upper:
    errors.append("Must contain an uppercase letter.")
if not has_digit:
    errors.append("Must contain a digit.")
if not has_special:
    errors.append("Must contain a special character.")

lower_password = password.lower()
if "password" in lower_password:
    errors.append("Must not contain the word 'password'.")

if errors:
    print("Password does not meet the sample policy:")
    for error in errors:
        print("-", error)
else:
    print("Password meets the sample policy.")

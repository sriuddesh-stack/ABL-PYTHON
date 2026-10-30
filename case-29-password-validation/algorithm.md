# Algorithm — Password Policy Validation Engine

Use a made-up sample password for this classroom exercise. Do not enter a personal password.

1. Start the program.
2. Read the sample password.
3. Create an empty list to store validation errors.
4. Initialize lowercase, uppercase, digit, and special-character flags to false.
5. Examine each character in the password.
6. Set the corresponding flag when a lowercase letter, uppercase letter, digit, or special character is found.
7. Check whether the password contains at least 8 characters. If not, add a length error.
8. Check whether each required character category was found. Add an error for every missing category.
9. Convert the password to lowercase and check whether it contains the prohibited word `password`. If it does, add an error.
10. If the error list is not empty, display all validation errors.
11. Otherwise, display that the sample password meets the policy.
12. Stop.

**Output:** A list of failed password rules or a policy-passed message.

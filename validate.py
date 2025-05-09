import re


email = input("What's your email? ").strip()

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.ed$", email):
    print("Valid")
else:
    print("Invalid")
    
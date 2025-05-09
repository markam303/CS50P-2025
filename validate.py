import re


email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|net|pl|org)$", email):
    print("Valid")
else:
    print("Invalid")
    
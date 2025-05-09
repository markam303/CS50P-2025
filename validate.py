import re


email = input("What's your email? ").strip()

if re.search(r"^[a-z0-9_\.]+@(\w+\.)?\w+\.(com|edu|net|pl|org)$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
    
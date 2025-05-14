import re


url = input("URL: ").strip()

# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
# print(f"Username: {username}")

if matches := re.search(r"^https://(?:www\.)?twitter\.(com|org)/([a-z0-9_]+)$", url, re.IGNORECASE):
   # if matches.group(1) == "com":
    print(f"Username:", matches.group(1))
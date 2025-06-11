import re

# extract username from url https://twitter.com/davidjmalan

url = input("Enter your twitter URL: ").strip()

#username = url.removeprefix("https://twitter.com/")

#cleaning data
#username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "",  url)

#matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
#print(f"Username: {matches.group(2)}")

# www  twitter usernames only alphanumerical and _
if matches:= re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")


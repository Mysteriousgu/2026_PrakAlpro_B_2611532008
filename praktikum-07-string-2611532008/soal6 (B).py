full_name = "Muhammad Rafi Firdaus"
nim = ""
# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().

clean = full_name.strip()
space = clean.find(" ")

if space == -1:
    first_name = clean
else:
    first_name = clean[:space]

username = first_name.lower() + nim[-3:]
print(username)
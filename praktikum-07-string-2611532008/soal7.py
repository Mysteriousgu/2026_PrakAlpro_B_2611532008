# Name: Muhammad Rafi Firdaus
# NIM: 2611532008
# Question 7

full_name = "muhammad rafi firdaus"
nim = "2611532008"
username = "Muhammad008"

intake = nim[0:2]           

W = 30
line = "=" * W

print(line)
print("STUDENT CARD".center(W))
print(line)
print(f"{'Name':<10}: {full_name.title()}")
print(f"{'NIM':<10}: {nim}")
print(f"{'Username':<10}: {username}")
print(f"{'Intake':<10}: {'20' + intake}")
print(line)
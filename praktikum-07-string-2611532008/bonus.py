# Name: Muhammad Rafi Firdaus
# NIM: 2611532008
# Bonus

kalimat = input("Masukkan kalimat: ")

bersih = kalimat.replace(" ", "").lower()

if bersih == bersih[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
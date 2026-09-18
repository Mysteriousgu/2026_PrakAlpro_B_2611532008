# Buat file dengan nama logika_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: a1_1234
# Program ini menggunakan fungsi input ()
# Program operator logika dalam python

# Memasukkan nilai boolean 
# Input tidak peka terhadap huruf besar dan kecil
a1_2008 = input ("Input nilai boolean-1 (true/false):  ").strip().lower() == "true"
a2_2008 = input ("Input nilai boolean-2 (true/false):  ").strip().lower() == "true"

print("\nA1 =", a1_2008)
print("A2 =", a2_2008)

# Konjungsi: Bernilai true jika keduanya True
hasil_2008 = a1_2008 and a2_2008
print("\nKonjungsi1 (AND)")
print("A1 dan A2 = ", hasil_2008)

# Disjungsi: Bernilai true jika salah satu True
hasil_2008 = a1_2008 or a2_2008
print("\nDisjungsi1 (OR)")
print("A1 or A2 = ", hasil_2008)

# Negasi A1: membalik nilai A1
hasil_2008 = not a1_2008
print("\nNegasi A1 (NOT)")
print("not A1 = ", hasil_2008)

# Negasi A2: membalik nilai A2
hasil_2008 = not a2_2008
print("\nNegasi A2 (NOT)")
print("not A2 = ", hasil_2008)

# XOR: Bernilai True jika kedua nilai berbeda
hasil_2008 = a1_2008 != a2_2008
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2 = ", hasil_2008)

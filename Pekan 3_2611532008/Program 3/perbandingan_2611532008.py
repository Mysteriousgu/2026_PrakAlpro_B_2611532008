# Buat file dengan nama perbandingan_nim.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan input ()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator perbandingan dalam python

angka1_2008 = int(input("Input angka-1: "))
angka2_2008 = int(input("Input angka-2: "))

# Lebih besar dari
hasil_2008 = angka1_2008 > angka2_2008
print("\nOperator lebih besar dari")
print("angka1 > angka2 =", hasil_2008)

# Lebih kecil dari
hasil_2008 = angka1_2008 < angka2_2008
print("\nOperator lebih kecil dari")
print("angka1 < angka2 =", hasil_2008)

# Lebih besar dari atau sama dengan
hasil_2008 = angka1_2008 >= angka2_2008
print("\nOperator lebih besar dari atau sama dengan")
print("angka1 >= angka2 =", hasil_2008)

# Lebih kecil dari atau sama dengan
hasil_2008 = angka1_2008 <= angka2_2008
print("\nOperator lebih kecil dari atau sama dengan")
print("angka1 <= angka2 =", hasil_2008)

# Sama dengan
hasil_2008 = angka1_2008 == angka2_2008
print("\nOperator sama dengan")
print("angka1 == angka2 =", hasil_2008)

# Tidak sama dengan
hasil_2008 = angka1_2008 != angka2_2008
print("\nOperator tidak sama dengan")
print ("angka1 != angka2 =", hasil_2008)

# Tambahan: perbandingan berantai dalam python
hasil = 0 < angka1_2008 < 100
print("\nPerbandingan berantai")
print("0 < angka1 < 100 =", hasil)

hasil = 0 < angka2_2008 < 100
print ("0 < angka2 < 100 =", hasil)


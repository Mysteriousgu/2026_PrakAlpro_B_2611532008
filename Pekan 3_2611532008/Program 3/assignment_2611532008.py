# Buat file dengan nama assignment_NIM.py
# Nama variabel ditambah 4 digit nim terkahir contoh: angka1_1234
# Program ini menggunakan fungsi input ()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer
# Program operator assignment dalam python

angka1_2008 = int(input("Input angka-1:  "))
angka2_2008 = int(input("Input angka-2:  "))

print("\nNilai awal angka1 =", angka1_2008)
print("NIlai angka2 = ", angka2_2008)

# Assignment biasa
hasil_2008 = angka1_2008
print("\nAssignment biasa (=)")
print("Hasil =", hasil_2008)

# Assignment penambahan
hasil_2008 = angka1_2008
hasil_2008 += angka2_2008
print("\nAssignment penambahan (+=)")
print("Hasil =", hasil_2008)

# Assignment pengurangan
hasil_2008 = angka1_2008
hasil_2008 -= angka2_2008
print("\nAssignment pengurangan (-=)")
print("Hasil =", hasil_2008)

# Assignment perkalian
hasil_2008 = angka1_2008
hasil_2008 *= angka2_2008
print("\nAssignment perkalian (*=)")
print("Hasil =", hasil_2008)

# Assignment pembagian, pembagian bulat, dan sisa bagi
if angka2_2008 != 0:
    hasil_2008 = angka1_2008
    hasil_2008 /= angka2_2008
    print("\nAssignment pembagian (/=)")
    print("Hasil =", hasil_2008)

    hasil_2008 = angka1_2008
    hasil_2008 //= angka2_2008
    print("\nAssignment pembagian bulat (//=)")
    print("Hasil =", hasil_2008)

    hasil_2008 = angka1_2008
    hasil_2008 %= angka2_2008
    print("\nAssignment sisa bagi (%=)")
    print("Hasil =", hasil_2008)
else:
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil_2008 = angka1_2008
hasil_2008 **= angka2_2008
print("\nAssignment perpangkatan (**=)")
print("Hasil =", hasil_2008)
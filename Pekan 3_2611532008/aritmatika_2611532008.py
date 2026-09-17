# Buat file dengan nama aritmatika_nim.py
# Buat program untuk operator aritmatika dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: angka_1234
# Program ini menggunakan input ()
# Nilai yang dimasukkan akan dikonversi menjadi tipe data integer

angka1_2008 = int(input("Input angka-1: "))
angka2_2008 = int(input("Input angka-2: "))

# Penjumlahan
hasil_2008 = angka1_2008 + angka2_2008  
print("\nOperator penjumlahan")
print("Hasil =", hasil_2008)

# Pengurangan 
hasil_2008 = angka1_2008 - angka2_2008
print("\nOperator pengurangan")
print("Hasil =", hasil_2008)

# Perkalian
hasil_2008 = angka1_2008 * angka2_2008
print("\nOperator perkalian")
print("Hasil =", hasil_2008)

# Pembagian, pembagian bulat, dan sisa bagi
if angka2_2008 != 0:
    hasil_2008 = angka1_2008 / angka2_2008
    print("\nOperator pembagian")
    print("Hasil =", hasil_2008)

    hasil_2008 = angka1_2008 // angka2_2008
    print("\nOperator pembagian bulat")
    print("Hasil =", hasil_2008)

    hasil_2008 = angka1_2008 % angka2_2008
    print("\nOperator sisa bagi")
    print("Hasil =", hasil_2008)
else:
    print("\nAngka kedua tidak boleh bernilai 0.")

# Pangkat
hasil_2008 = angka1_2008 ** angka2_2008
print("\nOperator pangkat")
print("Hasil =", hasil_2008)
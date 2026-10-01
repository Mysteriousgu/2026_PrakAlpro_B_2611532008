# Buat file dengan nama jumlah_genap_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: jumlah_1234
# Program ini menggunakan fungsi input()

ulang_2008 = int(input("Masukkan nilai batas: "))

jumlah_2008 = 0
for i in range(1, ulang_2008+1):
    if i % 2 == 0:
        print(i, end=" ")
        jumlah_2008 = jumlah_2008 + i

        if i < ulang_2008:
            print("+", end=" ")
        else:
            print(" = ", jumlah_2008, end=" ")
print()
print("Jumlah =", jumlah_2008)
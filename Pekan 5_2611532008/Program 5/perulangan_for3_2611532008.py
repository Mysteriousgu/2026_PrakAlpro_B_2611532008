# Buat file dengan nama perulangan_for3_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2008 = int(input("Masukkan jumlah perulangan: "))

jumlah_2008 = 0
for i_2008 in range(1, ulang_2008+1):
    print(i_2008, end=" ")
    jumlah_2008 = jumlah_2008 + i_2008

    if i_2008 < ulang_2008:
        print("+", end=" ")
    else:
        print(" = ", jumlah_2008, end=" ")
print()
print("Jumlah =", jumlah_2008)

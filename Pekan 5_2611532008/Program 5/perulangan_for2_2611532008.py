# Buat file dengan nama perulangan_for2_NIM
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2008 = int(input("Masukkan jumlah perulangan: "))
print("Perulangan ke-0 sampai ke-", ulang_2008-1)
for i_2008 in range(ulang_2008):
    print(i_2008, end="")
print()
print("Perulangan ke-1 sampai ke-", ulang_2008)
for i_2008 in range(1,ulang_2008+1):
    print(i_2008, end=" ")
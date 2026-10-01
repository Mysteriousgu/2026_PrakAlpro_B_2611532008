# Buat file dengan nama nested_for3_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2008 = int(input("Masukkan nilai batas: "))
for i_2008 in range(batas_2008+1):
    for j_2008 in range(batas_2008+1):
        print(i_2008+j_2008, end="  ")
    print()  # pindah ke baris berikutnya
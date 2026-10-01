# Buat file dengan nama nested_for1_NIM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2008 = int(input("Masukkan batas: "))
for line_2008 in range(1, batas_2008+1):
    for j_2008 in range(1, (-1 * line_2008 + batas_2008 + 1)):
        print(" . ", end="")
    print(line_2008)
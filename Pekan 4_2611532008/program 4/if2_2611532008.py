# Buat file dengan nama if2_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

ipk_2008 = float(input("Input IPK Anda = "))

if ipk_2008 > 2.75:
    print("Anda Lulus Sangat Memuaskan Dengan IPK " + str(ipk_2008))
else:
    print("Anda Tidak Lulus")
print("Program Selesai")

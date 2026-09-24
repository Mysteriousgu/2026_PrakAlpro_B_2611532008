# Buat file dengan nama if_elif_else1_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: ipk_1234
# Program ini menggunakan fungsi input()

umur_2008 = int(input("Input umur anda: "))
sim_2008 = input("Apakah anda sudah punya sim C: ")[0]

if umur_2008 >= 17 and sim_2008== 'y':
    print("Anda sudah dewasa dan boleh bawa motor")

elif umur_2008 >= 17 and sim_2008 != 'y':
    print ("Anda sudah dewasa tetapi tidak boleh bawa motor")

elif umur_2008 < 17 and sim_2008 =='y':
    print ("Anda belum cukup umur punya SIM")

else:
    print("Anda belum cukup umur dan tidak boleh bawa motor")
print("Program selesai")
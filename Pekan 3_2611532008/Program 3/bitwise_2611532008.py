# Buat file dengan nama bitwise_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input()

print ("\n======================")
print("3. OPERASI BITWISE")
print("=========================")

angka1_2008= int(input("Masukkan angka bitwise-1: "))
angka2_2008 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_2008, "| biner =", bin(angka1_2008))
print("angka2 =", angka2_2008, "| biner =", bin(angka2_2008))

# Bitwise AND
hasil_2008 = angka1_2008 & angka2_2008
print("\nBitwise AND (&)")
print(angka1_2008, "&", angka2_2008, "=", hasil_2008)
print("Biner hasil =", bin (hasil_2008))
print("Biner hasil (8 bit) =", format(hasil_2008, "08b"))

# Bitwise XOR
hasil_2008 = angka1_2008 ^ angka2_2008
print("\nBitwise XOR (^)")
print( angka1_2008, "^", angka2_2008, "=", hasil_2008)
print("Biner hasil =", bin(hasil_2008))
print("Biner hasil (8 bit) =", format (hasil_2008, "08b"))

# Bitwise NOT
hasil_2008 = ~angka1_2008
print("\nBitwise NOT (~)")
print("~", angka1_2008,  "=", hasil_2008)
print("Biner hasil =", bin(hasil_2008))
print("Biner hasil (8 bit) =", format (hasil_2008, "08b"))

#Bitwise geser kiri
jumlah_geser_2008 = int(input("\nMasukkan jumlah pergeseran bit"))

hasil_2008 = angka1_2008 << jumlah_geser_2008
print("\nBitwise geser kiri (<<)")
print(angka1_2008, "<<", jumlah_geser_2008, "=", hasil_2008)
print("Biner hasil =", bin (hasil_2008))
print("Biner hasil (8 Bit) =", format(hasil_2008, "08b"))

#Bitwise geser kanan
hasil_2008 = angka1_2008 >> jumlah_geser_2008
print("\nBitwise geser kanan (>>)")
print(angka1_2008, ">>", jumlah_geser_2008, "=", hasil_2008)
print("Biner hasil =", bin (hasil_2008))
print("Biner hasil (8 Bit) =", format(hasil_2008, "08b"))

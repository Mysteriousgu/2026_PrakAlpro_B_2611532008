# Buat file dengan nama lainnya_NIM.py
# Nama variabel ditambah 4 digit nim terakhir contoh: angka1_1234
# Program ini menggunakan fungsi input ()
# Program operator keanggotaan dan identitas

print("===============================")
print("OPERATOR KEANGGOTAAN")
print("===============================")

# Input beberapa data yang dipisahkan dengan koma
input_data_2008 = input ("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_2008 = [int(angka.strip()) for angka in input_data_2008.split(",")]

nilai_dicari_2008 = int(input("Masukkan angka yang ingin dicari:  "))

# Operator in
hasil_2008 = nilai_dicari_2008 in data_2008
print("\nOperator keanggotaan IN")
print(nilai_dicari_2008, "in", data_2008, "-", hasil_2008)

# Operator not in
hasil_2008 = nilai_dicari_2008 not in data_2008
print("\nOperator keanggotaan NOT IN")
print(nilai_dicari_2008, "not in", data_2008, "-", hasil_2008)

print("\n===============================")
print("2. OPERATOR IDENTITAS")
print("=================================")

# objek1 menggunakan list dari input pengguna
objek1_2008 = data_2008

# objek2 merujuk pada objek yang sama dengan objek1
objek2_2008 = objek1_2008

# objek3 memiliki isi sama, tetapi menggunakan objek baru
objek3_2008 = data_2008.copy()

print("objek1 = ", objek1_2008)
print("objek2 = ", objek2_2008)
print("objek3 = ", objek3_2008)

# Operator is
hasil_2008 = objek1_2008 is objek2_2008
print("\nOperator identitas IS")
print("objek1 is objek2 =", hasil_2008)

# Operator is not
hasil_2008 = objek1_2008 is not objek3_2008
print("\nOperator identitas IS NOT")
print("objek1 is not objek3 =", hasil_2008)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_2008 is objek3_2008)
print("objek1 == objek3 =", objek1_2008 == objek3_2008)


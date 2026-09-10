#Buat file dengan nama Boolean_2611532008.py
# Nama variabel ditambah 4 digit nim terakhir contoh: nilai_1234
# Deklarasi variabel dengan tipe data boolean
is_lulus_2008 = True
is_cumlaude_2008 = True

# Menggunakan Boolean
nilai_2008 = 80
batas_lulus_2008 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_2008 = nilai_2008 >= batas_lulus_2008  # Hasilnya akan true

print ("=== Check Kelulusan ===")
print ("Nilai:", nilai_2008)
print("Apakah lulus?:", status_kelulusan_2008)
if is_lulus_2008 and is_cumlaude_2008:
    print("Selamat, Anda lulus dengan predikat Cum Laude!")
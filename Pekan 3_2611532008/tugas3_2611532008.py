print("=== Sistem Simulasi Transaksi dan Validasi Akses Toko ===")

nama_2008 = input("Masukkan nama pelanggan : ")
status_2008 = input("Masukkan status pelanggan (Member/Nonmember) : ").lower()
total_belanja_2008 = float(input("Masukkan total belanja : Rp"))
jumlah_barang_2008 = int(input("Masukkan jumlah barang : "))
kode_promo_2008 = input("Masukkan kode promo : ").upper()

syarat_belanja_2008 = total_belanja_2008 >= 250000
syarat_barang_2008 = jumlah_barang_2008 >= 3
status_member_2008 = status_2008 == "Member"

daftar_promo_2008 = ["PROMO10.10", "30%OFF"]

promo_tersedia_2008 = kode_promo_2008 in daftar_promo_2008
promo_tidak_tersedia_2008 = kode_promo_2008 not in daftar_promo_2008

diskon_member_2008 = status_member_2008 and syarat_belanja_2008

promo_didapatkan_2008 = promo_tersedia_2008 and (syarat_belanja_2008 or syarat_barang_2008)

bukan_member_2008 = not status_member_2008

if diskon_member_2008:
    persentase_diskon_2008 = 0.10
else:
    persentase_diskon_2008 = 0.05 if syarat_belanja_2008 else 0

besar_diskon_2008    = total_belanja_2008 * persentase_diskon_2008

total_pembayaran_2008 = total_belanja_2008 - besar_diskon_2008

if jumlah_barang_2008 > 0:
    rata_rata_barang_2008 = total_belanja_2008 / jumlah_barang_2008
else:
    rata_rata_barang_2008 = 0

sisa_pembagian_2008 = int(total_belanja_2008) % jumlah_barang_2008 if jumlah_barang_2008 > 0 else 0


poin_2008 = 0
if status_member_2008:
    poin_2008 += int(total_pembayaran_2008 // 19999)

jumlah_barang_tersisa_2008 = jumlah_barang_2008
if promo_didapatkan_2008:
    jumlah_barang_tersisa_2008 -= 1

kode_1_2008 = ["PROMO10.10"]
kode_2_2008 = ["PROMO10.10"]
nilai_sama_2008 = kode_1_2008 == kode_2_2008
objek_sama_2008 = kode_1_2008 is kode_2_2008
objek_berbeda_2008 = kode_1_2008 is not kode_2_2008


kode_member_2008 = 1 if status_member_2008 else 0
kode_belanja_2008 = 2 if syarat_belanja_2008 else 0
kode_barang_2008 = 4 if syarat_barang_2008 else 0
kode_promo_2008 = 8 if promo_tersedia_2008 else 0

# Operator OR (|)
kode_status_2008 = (
    kode_member_2008
    | kode_belanja_2008
    | kode_barang_2008
    | kode_promo_2008
)

cek_member_2008 = kode_status_2008 & 1
cek_belanja_2008 = kode_status_2008 & 2
cek_barang_2008 = kode_status_2008 & 4
cek_promo_2008 = kode_status_2008 & 8

kode_referensi_2008 = 11
perbandingan_status_2008 = kode_status_2008 ^ kode_referensi_2008

kode_shift_2008 = kode_status_2008 << 1


member_access_2008 = bool(cek_member_2008)
promo_access_2008 = bool(cek_promo_2008)
free_shipping_access_2008 = syarat_belanja_2008 and syarat_barang_2008


print("\n=== DATA PELANGGAN ===")
print("Nama Pelanggan       :", nama_2008)
print("Status Pelanggan     :", status_2008)
print("Total Belanja        : Rp", total_belanja_2008)
print("Jumlah Barang        :", jumlah_barang_2008)
print("Kode Promo           :", kode_promo_2008)


print("\n=== HASIL VALIDASI ===")
print("Belanja >= Rp200000  :", syarat_belanja_2008)
print("Jumlah Barang >= 3   :", syarat_barang_2008)
print("Status Member        :", status_member_2008)
print("Kode Promo Tersedia  :", promo_tersedia_2008)
print("Mendapatkan Diskon   :", diskon_member_2008)
print("Mendapatkan Promo    :", promo_didapatkan_2008)


print("\n=== HASIL PERHITUNGAN ===")
print("Besarnya Diskon      : Rp", besar_diskon_2008)
print("Total Pembayaran     : Rp", total_pembayaran_2008)
print("Rata-rata Harga      : Rp", rata_rata_barang_2008)
print("Sisa Pembagian       :", sisa_pembagian_2008)


print("\n=== HAK AKSES PELANGGAN ===")
print("Kode Hak Akses       :", format(kode_status_2008, "04b"))
print("Member Access        :", member_access_2008)
print("Promo Access         :", promo_access_2008)
print("Free Shipping Access :", free_shipping_access_2008)
print("Poin Pelanggan       :", poin_2008)


print("\n=== OPERATOR IDENTITAS ===")
print("kode_1 == kode_2     :", nilai_sama_2008)
print("kode_1 is kode_2     :", objek_sama_2008)
print("kode_1 is not kode_2 :", objek_berbeda_2008)


print("\n=== OPERASI BITWISE ===")
print("Kode Status Transaksi")
print("0001 | 0010 | 0100 | 1000")

print("Kode Biner           :", format(kode_status_2008, "04b"))
print("Kode Desimal         :", kode_status_2008)

print("\n=== PEMERIKSAAN STATUS ===")

print("\nCek Member")
print(format(kode_status_2008, "04b"), "& 0001")
print("Hasil Biner         :", format(cek_member_2008, "04b"))
print("Hasil Desimal       :", cek_member_2008)

print("\nCek Belanja")
print(format(kode_status_2008, "04b"), "& 0010")
print("Hasil Biner         :", format(cek_belanja_2008, "04b"))
print("Hasil Desimal       :", cek_belanja_2008)

print("\nCek Jumlah Barang")
print(format(kode_status_2008, "04b"), "& 0100")
print("Hasil Biner         :", format(cek_barang_2008, "04b"))
print("Hasil Desimal       :", cek_barang_2008)

print("\nCek Promo")
print(format(kode_status_2008, "04b"), "& 1000")
print("Hasil Biner         :", format(cek_promo_2008, "04b"))
print("Hasil Desimal       :", cek_promo_2008)

print("\n=== PERBANDINGAN STATUS (XOR) ===")
print("Kode Transaksi      :", format(kode_status_2008, "04b"))
print("Kode Referensi      :", format(kode_referensi_2008, "04b"))
print(format(kode_status_2008, "04b"), "^",
      format(kode_referensi_2008, "04b"))
print("Hasil Biner         :", format(perbandingan_status_2008, "04b"))
print("Hasil Desimal       :", perbandingan_status_2008)

print("\n=== SHIFT ===")
print(format(kode_status_2008, "04b"), "<< 1")
print("Hasil Biner         :", format(kode_shift_2008, "b"))
print("Hasil Desimal       :", kode_shift_2008)

print("\n=== SELESAI ===")
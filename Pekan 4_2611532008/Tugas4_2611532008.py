# Program Sistem loket terpadu & Audit transaksi ekspedisi wahana

# 1 Input data pengunjung
print ("=== SISTEM LOKET ALPRO  ADVENTURE PARK===")
nama_pengunjung_2008 = str (input("Input Nama Anda: "))
umur_pengunjung_2008 = int (input("Input Umur Anda: "))
sim_2008 = input("Apakah Anda Sudah Mempunyai SIM C (y/t): ").strip().lower()




# 2 Pemilihan Wahana
print("\nPilihan Paket Wahana")
print(" 1. Wahana Safari Simba (Rp 50,000)")
print(" 2. Wahana Arung Jeram (Rp 75,000)")
print(" 3. Wahana Motor ATV Ekstrem (Rp 120,000)")
print(" 4. Wahana Roller Coaster Kilat (Rp 100,000)")
print(" 5. Wahana All-Access VIP (Rp 220,000)")

paket_2008 = int(input("Masukkan nomor paket: "))
match paket_2008:
    case 1: 
        nama_wahana_2008 = "Wahana Safari Simba"
        harga_wahana_2008 = 50000
    case 2:
        nama_wahana_2008 = "Wahana Arung Jeram"
        harga_wahana_2008 = 75000
    case 3:
        nama_wahana_2008 = "Wahana Motor ATV Ekstrem"
        harga_wahana_2008 = 120000
    case 4:
        nama_wahana_2008_2008 = "Wahana Roller Coaster Kilat"
        harga_wahana_2008 = 100000
    case 5:
        nama_wahana_2008 = "Wahana All-Access VIP"
        harga_wahana_2008 = 220000
    case _:
        print("Paket wahana tidak valid!")

jumlah_tiket_2008 = int(input("\nMasukkan jumlah tiket: "))
if jumlah_tiket_2008 <= 0:
    print("Kuota tiket tidak valid!")
input_member_2008 =  input("\nApakah Anda Member? (y/t): ").strip().lower()
is_member_2008 = input_member_2008 in ("y", "ya")
input_kode_promo_valid_2008 = input("Apakah Kode Promo Valid? (y/t): ").strip().lower()
kode_promo_valid_2008 = input_kode_promo_valid_2008 in ("y", "ya")

# 3 Validasi izin kendali wahana
print("\n---KELAYAKAN PENGENDARA WAHANA---")

if paket_2008 == 3 and umur_pengunjung_2008 >= 17 and sim_2008 == 'y':
    status_akses_2008 = ("Anda Sudah Dewasa Dan Boleh Mengendarai ATV Sendiri.")
elif paket_2008 == 3 and umur_pengunjung_2008 >= 17 and sim_2008 != 'y':
    status_akses_2008 = ("Anda Sudah Dewasa Tetapi Tidak Boleh Bawa Motor ATV \n(Wajib Didampingi Instruktur)")
elif paket_2008 == 3 and umur_pengunjung_2008 < 17 and sim_2008 == 'y':
    status_akses_2008 = ("Identitas tidak valid: Belum cukup umur memiliki SIM")
elif paket_2008 == 3 and umur_pengunjung_2008 <17 and sim_2008 != 'y':
    status_akses_2008 = ("Anda Belum Cukup Umur Dan Tidak Boleh Membawa ATV")
elif umur_pengunjung_2008 >= 10:
    status_akses_2008 = ("Anda boleh masuk wahana ini")
else:
    status_akses_2008 = ("Umur anda tidak cukup untuk wahana ini")

print (f"Status Akses: {status_akses_2008}")


# 4 Akumulasi Diskon
# Subtotal 
subtotal_2008 = harga_wahana_2008 * jumlah_tiket_2008

total_diskon_persen_2008 = 0

# Diskon Belanja Besar
if float(subtotal_2008) >= 200000 : 
    total_diskon_persen_2008 += 10
# Diskon member
if is_member_2008:
    total_diskon_persen_2008 += 5
# Diskon Voucher Promo
if kode_promo_valid_2008:
    total_diskon_persen_2008 += 15
# Diskon Tambahan Rombongan
if jumlah_tiket_2008 >= 5:
    total_diskon_persen_2008 += 5

# 5. Evaluasi Kelulusan

# Penghitungan total bayar
nominal_diskon_2008 = subtotal_2008 * (total_diskon_persen_2008 / 100)
total_bayar_2008 = subtotal_2008 - nominal_diskon_2008

# Catatan Layanan 
if total_bayar_2008 > 300000:
    catatan_layanan_2008 = ("Selamat! Anda berhak mendapat Souvenir Gratis.")
else:
    catatan_layanan_2008 = ("Terima Kasih Telah Berkunjung.")

# Rincian pembayaran
print("\n---Rincian Pembayaran---")
print(f"Subtotal Belanja : Rp{subtotal_2008: ,.0f}")
print(f"Total Diskon : {total_diskon_persen_2008}% (Rp{nominal_diskon_2008:,.0f})")
print(f"Total Bayar : Rp {total_bayar_2008:,.0f}")
print(f"Catatan Layanan : {catatan_layanan_2008}")
print("\nProgram Selesai")
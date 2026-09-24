# Buat file dengan nama multi_if_nim.py
# Buat program untuk kondisional if
# Nama variabel ditambah 4 digit nim terakhir contoh: total_belanja_1234
# Program ini menggunakan fungsi input ()
# Program menghitung diskon belanja

# Input dari user
total_belanja_2008 = float(input("Masukkan total belanja (Rp): "))

# Input status member (Mengecek apakah user mengetik 'y' atau 'ya')
input_member_2008 = input("Apakah anda member? (y/t): ").strip().lower()
is_member_2008 = input_member_2008 in ("y", "ya")

# Input Status kode promo (Mengecek apakah user mengetik 'y' atau 'ya')
input_promo_2008 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_2008 = input_promo_2008 in ("y", "ya")

total_diskon_persen_2008 = 0

# Multi-if Terpisah: Setiap kondisi diperiksa secara independen
# Diskon bisa ditumpuk (akumulasi) jika memenuhi syarat sekaligus

if total_belanja_2008 > 1000000:
    total_diskon_persen_2008 += 10  # Diskon belanja BytesWarning

if is_member_2008:
    total_diskon_persen_2008 += 5 # Diskon member

if kode_promo_valid_2008:    
    total_diskon_persen_2008 += 15 # Diskon voucher

# Menghitung nominal diskon dan total bayar
nominal_diskon_2008 = total_belanja_2008 * (total_diskon_persen_2008 / 100)
total_bayar_2008 = total_belanja_2008 - nominal_diskon_2008

# Output hasil
print("\n--- Rincian Pembayaran ---")
print(f"Total Diskon : {total_diskon_persen_2008} % (Rp {nominal_diskon_2008:,.0f})")
print(f"Total Bayar : Rp {total_bayar_2008:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_2008}%")
# Output: Total diskon yang anda dapatkan: 30% jika belanja > 1 Juta, member, dan kode promo valid
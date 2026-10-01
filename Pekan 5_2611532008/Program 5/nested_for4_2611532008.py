# Buat file dengan nama nested_for4_NiM.py
# Buat program untuk perulangan for dalam python
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_2008 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2008 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2008 = tinggi_2008
    c_2008 = a_2008
    lebar_2008 = (2 * tinggi_2008) - 2

    for i_2008 in range(1, tinggi_2008 + 1):
        b_2008 = c_2008 + 1

        for j_2008 in range(1, lebar_2008 +1):

            # Baris atas dan bawah
            if i_2008 == 1 or i_2008 == tinggi_2008:
                if j_2008 == 1 or j_2008 == lebar_2008:
                    print("#", end="")
                else:
                    print("=", end="")
                # Baris isi
            else:
                if j_2008 == 1 or j_2008 == lebar_2008:
                    print("|", end="")
                else:
                    if j_2008 == c_2008:
                        print("<", end="")
                    elif j_2008 == b_2008:
                        print(">", end="")
                    elif j_2008 == (lebar_2008 - c_2008):
                        print("<", end="")
                    elif j_2008 == (lebar_2008 - c_2008 +1):
                        print(">", end="")
                    elif j_2008 > b_2008 and j_2008 < (lebar_2008 - c_2008):
                        print(",", end="")
                    else:
                        print(" ", end="")


        print()

        # Logika asli Java
        a_2008 -= 2

        if a_2008 <= 0:
            c_2008 = (-a_2008) + 2
        else: 
            c_2008 = a_2008





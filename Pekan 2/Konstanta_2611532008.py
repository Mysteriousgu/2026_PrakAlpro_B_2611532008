#Buat file dengan nama Konstanta_2611532008.py
# Program ini menggunakan konstanta untuk menghitung luas lingkaran
# Nama variable ditambah 4 digit nim terakhir contoh: jari_1234

from typing import Final

PI_2008: Final[float] = 3.14
print("PI_2008: %f" % (PI_2008))
jari_2008 = float(input("Masukkan jari-jari: "))
luas_2008 = PI_2008 * jari_2008 * jari_2008
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2008, luas_2008))
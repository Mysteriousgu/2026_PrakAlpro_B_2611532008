# Program tinggi segitiga
tinggi_2008 = int(input("Masukkan tinggi segitiga: "))
for i_2008 in range(1, tinggi_2008 + 1):
    print(" " * (tinggi_2008 - i_2008), end="")
    
    for j_2008 in range(i_2008):

        print("*", end=" ")
    print() # pindah ke baris berikutnya

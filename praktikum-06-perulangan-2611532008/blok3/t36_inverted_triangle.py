tinggi = int(input("Masukkan tinggi segitiga: "))
for row in range(tinggi, 0, -1):
    for column in range(row):
        print("*", end=" ")
    print()
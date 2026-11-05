blocked_seats = int(input("Masukkan jumlah kursi yang diblokir: "))

for row in range (1, 4):
    print ("Row", row, end=": ")

    for column in range (1,6):
        if column == blocked_seats:
            break
        print (column, end=" ")
    print()
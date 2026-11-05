total = 0
while True:
    number = int(input("Enter a number: "))
    
    if number < 0:
      break
    
    # Bilangan 0 dilewati
    elif number == 0:
        continue
    
    # Bilangan positif ditampilkan dan dijumlahkan
    else:
        print("Positive number:", number)
        total += number

# Setelah loop selesai, tampilkan total
print("Total: ", total)  
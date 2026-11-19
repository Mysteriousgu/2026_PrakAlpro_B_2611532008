#Soal_8
number_of_rows = 4
seats_per_row = 5

seats = []
for r in range(number_of_rows):
    row = []
    for s in range(seats_per_row):
        row.append(".")
    seats.append(row)

taken = 0

while True:
    for r in range(number_of_rows):
        print(f"Row {r + 1}:", " ".join(seats[r]))

    row_number = int(input("Row (0 to stop): "))
    if row_number == 0:
        break

    seat_number = int(input("Seat: "))

    
    if row_number < 1 or row_number > number_of_rows or seat_number < 1 or seat_number > seats_per_row:
        print("Invalid seat.")
    elif seats[row_number - 1][seat_number - 1] == "X":
        print("Seat already taken.")
    else:
        seats[row_number - 1][seat_number - 1] = "X"
        taken += 1
        print("Seat booked.")

print("Seats taken:", taken)
#Soal_7
menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []

for day in range(1, number_of_days + 1):
    row = []
    for menu in menus:
        portion = int(input(f"Day {day}, {menu}: "))
        row.append(portion)
    sales.append(row)

print("Total per day:")
for i in range(len(sales)):
    day_total = 0
    for portion in sales[i]:
        day_total += portion
    print(f"Day {i + 1}: {day_total}")

menu_totals = []
for column in range(len(menus)):
    menu_total = 0
    for row in range(len(sales)):
        menu_total += sales[row][column]
    menu_totals.append((menus[column], menu_total))
print("Total per menu:", menu_totals)

best_name = menu_totals[0][0]
best_total = menu_totals[0][1]
for name, total in menu_totals:
    if total > best_total:   
        best_name = name
        best_total = total
print(f"Best seller: {best_name} ({best_total})")
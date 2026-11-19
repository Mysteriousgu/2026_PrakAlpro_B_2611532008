#Soal_6
LAST_DIGIT = 8  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []

# Baca 7 pengeluaran
for day in range(1, 8):
    value = int(input(f"Day {day}: "))
    expenses.append(value)

total = 0
highest = expenses[0]
highest_day = 1
days_above = 0

for i in range(len(expenses)):
    total += expenses[i]

    if expenses[i] > highest:
        highest = expenses[i]
        highest_day = i + 1

    if expenses[i] > daily_limit:
        days_above += 1

average = total / len(expenses)

print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {average:.1f}")
print(f"Highest: day {highest_day} ({highest})")
print(f"Days above limit: {days_above}")
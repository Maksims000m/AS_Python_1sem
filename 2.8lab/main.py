# Функцианирует только если даты написаны "дд.мм.гггг", например: "12.12.2012"

def is_spring_date(day, month):
    return month in [3, 4, 5]

def find_spring_dates(filename):
    spring_dates = []

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                day, month, year = map(int, parts)
                if is_spring_date(day, month):
                    spring_dates.append(f"{day:02d} {month:02d} {year}")

    return spring_dates

# Требуется файл с датами
filename = 'dates.txt'
spring_dates = find_spring_dates(filename)


print("Весенние даты:")
for date in spring_dates:
    print(date)


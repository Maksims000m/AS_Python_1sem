def quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    else:
        raise ValueError("Координаты должны быть ненулевыми.")
try:
    x = float(input("Введите координату x: "))
    y = float(input("Введите координату y: "))
    result = quarter(x, y)
    print(f"Точка ({x}, {y}) находится в {result}-й четверти.")
except ValueError as e:
    print(e)

class InvalidHeightError(Exception):
    pass
class InvalidWeightError(Exception):
    pass
class InvalidTemperatureError(Exception):
    pass
def check_height():
    height = float(input("Введите ваш рост в см: "))
    if height < 0 or height > 300:
        raise InvalidHeightError("Некорректный рост")
    else:
        print("Рост введен корректно")
def check_weight():
    weight = float(input("Введите ваш вес в кг: "))
    if weight < 0 or weight > 500:
        raise InvalidWeightError("Некорректный вес")
    else:
        print("Вес введен корректно")
def check_temperature():
    temperature = float(input("Введите температуру в градусах Цельсия: "))
    if temperature < -273.15:
        raise InvalidTemperatureError("Некорректная температура")
    else:
        print("Температура введена корректно")
def main():
    try:
        check_height()
    except InvalidHeightError as e:
        print(e)
    try:
        check_weight()
    except InvalidWeightError as e:
        print(e)
    try:
        check_temperature()
    except InvalidTemperatureError as e:
        print(e)
if __name__ == "__main__":
    pass

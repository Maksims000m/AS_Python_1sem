if __name__ == "__main__":
    s=float(input("Цена за 1 кг конфет: "))
    for kg in [1.2, 1.4, 1.6, 1.8, 2.0]:
        t=s*kg
        print(f"{kg} кг - {t:.2f}руб.")

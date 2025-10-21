if __name__ == "__main__":
    print("Задание №1")
    K=int(input("Введите K:"))
    N=int(input("Введите N:"))
    for in range (N):
        print(K)
    print("Задание №2")

    
    A=int(input("Введите A:"))
    B=int(input("Введите B:"))
    numbers = list(range(A, B + 1))
    print(*numbers)
    print("Количество чисел: ", len(numbers))

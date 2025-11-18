def SwapCol(A, K1, K2):
    if K1 < 0 or K2 < 0 or K1 >= len(A[0]) or K2 >= len(A[0]):
        raise IndexError("Индексы столбцов выходят за пределы матрицы")
    for row in A:
        row[K1], row[K2] = row[K2], row[K1]
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Первоначальная матрица:")
    for row in matrix:
        print(row)

    SwapCol(matrix, 0, 2)
    print("Матрица после обмена столбцов:")
    for row in matrix:
        print(row)

import numpy as np

def read_matrices_from_file(filename):
    with open(filename, 'r') as file:
        data = file.read().strip().split('\n\n')
        matrices = []
        for block in data:
            matrix = []
            for line in block.strip().split('\n'):
                matrix.append(list(map(float, line.split())))
            matrices.append(np.array(matrix))
    return matrices

def write_results_to_file(filename, results):
# Требуется пустая строка между матрицами
    with open(filename, 'w') as file:
        for mat1, mat2, result in results:
            np.savetxt(file, mat1, fmt='%.2f')
            file.write('\n') 
            np.savetxt(file, mat2, fmt='%.2f')
            file.write('\n') 
            np.savetxt(file, result, fmt='%.2f')
            file.write('\n\n') 

# требуется название файлов

def main():
    matrices_a = read_matrices_from_file('file1.txt') 
    matrices_b = read_matrices_from_file('file2.txt') 

    if len(matrices_a) != len(matrices_b):
        raise ValueError("Количество матриц в файлах должно совпадать.")

    results = []

    for mat_a, mat_b in zip(matrices_a, matrices_b):
        result = np.dot(mat_a, mat_b) 
        results.append((mat_a, mat_b, result))

    write_results_to_file('results.txt', results)

    print("Содержимое первого файла (file1.txt):")
    with open('file1.txt', 'r') as f:
        print(f.read())

    print("\nСодержимое второго файла (file2.txt):")
    with open('file2.txt', 'r') as f:
        print(f.read())

    print("\nСодержимое третьего файла (results.txt):")
    with open('results.txt', 'r') as f:
        print(f.read())

if __name__ == "__main__":
    main()


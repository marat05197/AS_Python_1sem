def read_matrices(filename, n):
    matrices = []
    with open(filename, 'r') as f:
        while True:
            matrix = []
            for i in range(n):
                line = f.readline()
                if not line:
                    return matrices
                row = list(map(int, line.split()))
                matrix.append(row)
            matrices.append(matrix)

def diagonal_product(matrix):
    product = 1
    for i in range(len(matrix)):
        product *= matrix[i][i]
    return product

n = int(input("Введите размерность матриц n: "))
k = int(input("Введите количество матриц k: "))
limit = int(input("Введите заданное число: "))

matrices = read_matrices('input.txt', n)

with open('output.txt', 'w') as f_out:
    for matrix in matrices:
        if diagonal_product(matrix) > limit:
            for row in matrix:
                f_out.write(' '.join(map(str, row)) + '\n')
            f_out.write('\n')

print("Содержимое исходного файла:")
with open('input.txt', 'r') as f:
    print(f.read())

print("Содержимое выходного файла:")
with open('output.txt', 'r') as f:
    print(f.read())

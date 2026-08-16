import random


def generate_matrix(rows, cols, low=-50, high=50):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(low, high))
        matrix.append(row)
    return matrix


def add_matrices(m1, m2):
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[0])):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result


rows = 10
cols = 10

matrix_1 = generate_matrix(rows, cols)
matrix_2 = generate_matrix(rows, cols)
matrix_3 = add_matrices(matrix_1, matrix_2)

print(matrix_1)
print(matrix_2)
print(matrix_3)
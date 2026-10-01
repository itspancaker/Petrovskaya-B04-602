import numpy as np
n, m = map(int, input().split())
matrix = np.zeros((n, m))
print("Вводите числа по очереди:")
for i in range(n):
    for j in range(m):
        matrix[i, j] = float(input(f"Элемент в строке {i+1}, столбце {j+1}: "))
num_variables = m - 1
A = matrix[0:n, 0:num_variables]
B = matrix[0:n, num_variables]
X = np.linalg.solve(A, B)
print("\nОтвет:")
print(X)
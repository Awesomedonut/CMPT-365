import numpy as np

def dct_matrix(N):
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i == 0:
                a = 1 / np.sqrt(N)
            else:
                a = np.sqrt(2 / N)
            matrix[i, j] = a * np.cos((np.pi * (2 * j + 1) * i) / (2 * N))
    return matrix

# The dequantized matrix
val_matrix = np.array([[60, 47, 56, 0, 88, 0, 0, 0],
                       [0, 0, 0, 48, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 28, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]])

# Calculate the DCT matrix
dct_matrix_8x8 = dct_matrix(8)
print("dct matrix:")
print(dct_matrix_8x8)

# Perform the IDCT by matrix multiplication
idct_result = np.dot(np.dot(dct_matrix_8x8.T, val_matrix), dct_matrix_8x8)

# Round the result to integer values or desired precision
rounded_idct_result = np.round(idct_result).astype(int)

print("final res:")

print(rounded_idct_result)

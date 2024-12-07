import numpy as np

def one_dim_dct(strip):
    N = len(strip)
    coeffs = np.zeros(N)
    
    for i in range(N):
        element = 0
        for j in range(N):
            
            term1 = 2 * j + 1 # 2j + 1
            term2 = i * np.pi # i * π
            term3 = 2 * N # 2N
            
            angle = (term2 * term1) / term3
            cos_term = np.cos(angle)
            element += strip[j] * cos_term
        
        if i == 0: # √(1/N)
            a = np.sqrt(1/N)
        else: # if i > 0, √(2/N)
            a = np.sqrt(2/N)

        coeffs[i] = element * a
            
    return coeffs

def rows_first(matrix):
    rf_matrix = matrix.shape[0]
    final_coeffs = np.zeros_like(matrix, dtype=float)
    
    for i in range(rf_matrix): # i = rows, so rows first
        final_coeffs[i, :] = one_dim_dct(matrix[i, :])
    
    for j in range(rf_matrix): #j = cols, cols last
        final_coeffs[:, j] = one_dim_dct(final_coeffs[:, j])
        
    return np.round(final_coeffs).astype(int)

def cols_first(matrix):
    cf_matrix = matrix.shape[1]
    final_coeffs = np.zeros_like(matrix, dtype=float)
    
    for j in range(cf_matrix): #cols
        final_coeffs[:, j] = one_dim_dct(matrix[:, j])
    
    for i in range(cf_matrix): #rows
        final_coeffs[i, :] = one_dim_dct(final_coeffs[i, :])
        
    return np.round(final_coeffs).astype(int)

print("please enter an int between 2 and 8 for the N value:")
N = int(input())




print("please enter the matrix elements. Seperate elements with a comma (,) and rows with a semicolon (;) :")
matrix_str = input()
rows = [row.strip() for row in matrix_str.split(';') if row.strip()]

matrix = []
for row in rows:
    values = [int(x.strip()) for x in row.split(',') if x.strip()]
    matrix.append(values)

matrix = np.array(matrix)

print("rows first then columns DCT:")
result1 = rows_first(matrix)
print(result1)

print("columns first then rows DCT:")
result2 = cols_first(matrix)
print(result2)

print("\nAre results identical?", np.array_equal(result1, result2))

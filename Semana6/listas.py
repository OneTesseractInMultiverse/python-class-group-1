def suma(x, y):
    return x + y
"""
lista_ejemplo = ["hilera de texto", 2344, 2344.29, None,  False, suma]
for elemento in lista_ejemplo: print(elemento)
print(len(lista_ejemplo))
resultado = lista_ejemplo[-1](50, 70)
print(resultado)
print(lista_ejemplo[-3])
texto = "Hola, tengo hambre!"
lista_ejemplo = ["hilera de texto", 2344, 2344.29, None,  False, suma, 23, "h"]
print(lista_ejemplo[2:5])
"""

def print_matrix_impura(matrix):
    for fila in matrix:
        print(fila)

def matrix_to_string(matrix):
    result = ""
    for fila in matrix:
        result += str(fila) + "\n"
    return result

def mark_diagonal(matrix):
    for fila in range(0, len(matrix)):
        for columna in range(0, len(matrix[fila])):
            if fila == columna:
                matrix[fila][columna] = 1
    return matrix

def generar_matrix(filas, columnas):
    mi_lista_de_listas = []
    for numero in range(0, filas):
        mi_lista_de_listas.append([])
        for num in range(0, columnas):
            mi_lista_de_listas[numero].append(0)
    return mi_lista_de_listas




print(matrix_to_string(mark_diagonal(generar_matrix(20, 20))))

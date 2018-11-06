# Esto es una lista de números
lista_de_numeros = [1,2,3,4,12,23,45,56,67]

# lista vacía
lista_vacia = []
lista_vacia.append("Hola")
lista_vacia.append("otro")

for numero in range(0, 100):
    lista_vacia.append(str(numero))

# Podemos utilizar un índice para solicitar el elemento 
# que se encuentra en una posición determinada
print(lista_vacia[14])

# podemos consultar la cantidad de elementos que tiene una
# una lista
print(len(lista_vacia))
print(lista_vacia[len(lista_vacia) - 1])

lista_que_nunca_deberiamos_hacer = ["holas", 12, 234.123, ["12"], True]

def print_matrix(matrix):
    output = ""
    for fila in matrix:
        output += str(fila) + "\n"
    return output

def dibuje_diagonal_en_matriz(matrix):
    for fila in range(0,len(matrix)):
        for columna in range(0, len(matrix[fila])):
            if fila == columna:
                matrix[fila][columna] = '@'
    return matrix


matrix = [
#    0  1  2  3  4  5  6
    [0, 0, 0, 0, 0, 0, 0], # 0
    [0, 1, 0, 0, 0, 0, 0], # 1
    [0, 0, 0, 0, 0, 0, 0], # 2
    [0, 0, 0, 0, 0, 0, 0], # 3
    [0, 0, 0, 0, 0, 0, 0], # 4
    [0, 3, 0, 0, 0, 0, 0], # 5
    [0, 0, 0, 0, 0, 0, 0]  # 6
]
print(print_matrix(dibuje_diagonal_en_matriz(matrix)))

a = set([1, 2, 23, 34, 56, 76])
b = set([23, 47, 1, 32, 36, 90, 101, 23])

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

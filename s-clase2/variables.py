print("Hola, esto es una clase sobre variables en Python")
print("-----------------------------------------")
# Esto es un comentario de una sola línea

"""
A continuación vamos a crear un programa que nos permite
calcular un discriminante. El discriminante se puede 
calcular de la siguente manera:
dicriminante = (bˆ2) - 4(a)(c)
"""

# primero declaramos las variable a, b, c
a = 1
b = 8
c = 5

#(xˆ2) + 8x + 5

# ahora calculamos el discriminanto usando 
# la formula anterior y los operadores 
# aritméticos

discriminante = (b ** 2) - 4*a*c

print("El discriminante es: " + str(discriminante))
print("------------------------------------------")

numero_por_verificar = 122

es_par = (numero_por_verificar % 2) == (0)

print("El número es par: " + str(es_par))
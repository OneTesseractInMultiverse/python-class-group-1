"""
print(range(5,10))
total_impares = 0
# por cada [variable] in [range/collection]:
for numero in range(5, 27):
    if numero % 2 != 0:
        print(numero)
        total_impares+=1
print("El total de impares es {}".format(total_impares))

for num in range(1, 10):
    for factor in range(1, 10):
        resultado_multiplicacion = num * factor
        print("{} X {} = {}".format(num, factor, resultado_multiplicacion))

numero = 73
for divisor in (2, numero):
    if numero % divisor == 0 and numero != divisor:
        print("El {} no es primo porque es divisible entre {}".format(numero, divisor))
        break
"""

for numero in range(2, 100):

    # Para cada uno de estos números, verificar si es primo
    # o no es primo. Es primo, si solo es divisible entre 1
    # y entre si mismo. No es primo si es divisible entre entre
    # algún otro número. 
    es_primo = True
    for posible_divisor in range(2, numero):
        if numero % posible_divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(numero)



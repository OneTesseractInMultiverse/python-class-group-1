# Ejemplos de uso del if en python:

esta_lloviendo = True
tenemos_hambre = False
python_es_genial = True
ayer_pagaron = False
vamos_a_la_playa = False

# Función para solicitar datos por consola input("mensage")
# La función input siempre retorna un string. Tenemos que 
# convertirlo a número antes de hacer operaciones numéricas
numero_digitado = input("Digite un número: ") # Almaceno como string
numero_digitado_como_numero = int(numero_digitado)

if esta_lloviendo and tenemos_hambre:
    # Este código está dentro del if
    print("Está lloviendo y tenemos hambre")
elif (12 < numero_digitado_como_numero and python_es_genial) or vamos_a_la_playa:
    print("Python es genial o vamos a la playa")
else:
    print("Esto se ejecuta si ninguna condición anterior es verdadera")

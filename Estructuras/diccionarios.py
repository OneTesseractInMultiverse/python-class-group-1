import pprint


# Vamos a empezar declarando un diccionario vacío
diccionario_vacio = {}

# un diccionario con valores establecidos como literales
datos_personales = {
    "nombre": "John", 
    "apellido": "Smith",
    "edad": 20, 
    "carreras": [
        "Computación", 
        "Física"
    ],
    "universidad": {
        "nombre": "Universidad Super Patito",
        "fundación": 2001
    }
}

# Ahora vamos a preguntarle al diccionario cuales
# son las llaves que tiene
print(datos_personales.keys())

# Ahora vamos a acceder a los valores del diccionario
print(datos_personales["nombre"])

# Ahora vamos a modificar el valor de una llave que 
# se encuentra en el diccionario
datos_personales["nombre"] = "Jane"

# Ahora vamos a agregar una llave que no existía previamente
datos_personales["email"] = "jane.smith@example.com"
pprint.pprint(datos_personales)

# Vamos a imprimir todos los valores de todas las
# llaves que se cuentran en el diccionario
for key in datos_personales.keys():
    print(datos_personales[key])

# Diccionario dentro de un diccionario
print(datos_personales["universidad"]["nombre"])

# Lista dentro de un diccionario
print(datos_personales["carreras"][0])


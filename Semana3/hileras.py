# Tema Hileras

message = input("Digite lo que quiera: ")

print(message)

# len() -> Encontrar la cantidad de caracteres que tiene una hilera

print(len(message))

# Índices
print(message[0]) # Obtenemos el primer caracter de una hilera
print(message[len(message) - 1]) # Obtenemos el último caracter de una hilera

# Concatenación de hileras
hilera = "Hilera inicial"

# Concatenación simple
print(hilera + " otra hilera")
print(hilera)

# Concatenación modificando la variable
hilera += ". Esto sí modifica la variable hilera"
print(hilera)

# Inyectando texto 

otra_hilera = "Hola {} {}! ¿Cómo está? {} ".format("Pedro", "Guzmán", hilera)
print(otra_hilera)
print(otra_hilera[3:10])
print(otra_hilera[:10])
print(otra_hilera[10:])
print(otra_hilera[::-1])
 
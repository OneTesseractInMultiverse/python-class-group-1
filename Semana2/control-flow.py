"""
a = True
b = False
c = True
d = False

if ( a and b ) and not d:
    print("El caso 1 es verdadero")
elif c and b:
    print("El caso 2 es verdadero")
else:
    print("Ninguno es verdadero")

print("Esto siempre se ejecuta")
"""

response = 0
valid_response = False

while not valid_response:
    response = int(input("Ingrese un número impar mayor que 100: "))
    if response < 100:
        print("Debe ingresar un número mayor que 100")
    elif response % 2 is 0:
        print("El número debe ser impar")
    else:
        valid_response = True
        print("Muchas gracias por digitar un número")

# Un for con las letras de una palabra
output = ""
for letter in "Hola Mundo":
    if letter == "H" or letter == "M":
        output += letter.lower()
        # output = output + letter.lower()
    else:
        output += letter.upper()
print(output)

# --------------------------------------------------------
# For con un rango de números
# --------------------------------------------------------

# traten de evitar esto!!
suma = 0
for number in range(0, response):

    if number in [23, 45, 67, 76, 23, 978, 234, -12]:
        print("Lucky number found!")
    else:
      suma = suma + number  

print(suma)

# --------------------------------------------------------
# For con una lista de palabras
# --------------------------------------------------------

palaras = ["palabra1", "palabra2", "palabra3", "palabra4"]

for palabra in palaras:
    print(palabra.upper())









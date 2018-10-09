numero = int(input("Escriba un número: "))

max_value = numero // 2

# Asumimos primero que es primo y luego vamos a verificar si esto
# se mantiene válido al validar el número
es_primo = True
divisor = 2

while(divisor < max_value and es_primo):
    if numero % divisor == 0:
        es_primo = False
    else:
        divisor = divisor + 1
print("Es primo: {}".format(es_primo))





"""
Escriba un programa que encuentre todos los números 
que son divisibles entre 7 pero que no son múltiplos 
de 5 entre 2000 y 3200. 
"""

def es_divisible(numero, divisor) -> bool:
    """
        Si el número es divisible, retorna True. Si no es divisible, 
        entonces retorna False. 
    """
    return numero % divisor == 0

def extraer_numeros_divisibles_por_7_no_por_5(min, max):
    los_que_cumplen_la_condicion = [] # Creamos una lista vacía
    for numero in range(min, max + 1):
        if es_divisible(numero, 7) and not es_divisible(numero, 5):
            los_que_cumplen_la_condicion.append(numero)
    return los_que_cumplen_la_condicion


print(extraer_numeros_divisibles_por_7_no_por_5(2000, 3200))



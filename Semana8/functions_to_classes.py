# FUNCTION ELEVAR POTENCIA
def eleve_potencia(base, exponente):
    return float(base ** exponente)

# CALCULE EXPONENTE RADICAL
def calcule_exponente_radical(denominador):
    return float(1/denominador)

# FUNCION CALCULAR RAIZ
def calcular_raiz(raiz, numero):
    resultado = None
    if raiz > 0:
        raiz =  calcule_exponente_radical(raiz)
        resultado = eleve_potencia(numero, raiz)
    return resultado

# FUNCION CALCULE 4AC
def calcule_4ac(a, c):
    return (4*a*c)

# FUNCION CALCULAR DISCRIMINANTE
def calcular_discriminante(a, b, c):
    """
        El dicriminante se calcular como d = (b^2) - 4(a)(c)
    """
    b_cuadrado = eleve_potencia(base = b, exponente = 2)
    cuatro_ac = calcule_4ac(a, c)
    return float(b_cuadrado - cuatro_ac)

# FUNCIÓN NEGATIVO
def negativo(numero) -> float:
    return numero * -1

# CALCULAR INTERSECCIÓN CON EJE
def calcular_intersecion_con_eje(a, b, raiz_de_discriminante, raiz_disc_negativa: bool):
    resultado = None
    b = negativo(float(b))
    a = float(a)
    z = (2*a)
    if raiz_disc_negativa:
        resultado = (b - raiz_de_discriminante) / z
    else:
        resultado = (b + raiz_de_discriminante) / z
    return float(resultado)
    
    
# CALCULAR SOLUCIONES DE EQUACIÓN CUADRÁTICA
def calcular_soluciones(a, b, c):
    raiz_de_discriminante = calcular_raiz(2, calcular_discriminante(a,b,c))
    return {
        "x0": calcular_intersecion_con_eje(a, b, raiz_de_discriminante, True), 
        "x1": calcular_intersecion_con_eje(a, b, raiz_de_discriminante, False)
    }    

print(calcular_soluciones(a=1, b=5, c=6))
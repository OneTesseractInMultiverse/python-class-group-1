

# FUNCTION ELEVAR POTENCIA
def elevar_potencia(base: float, exponente: float) -> float:
    return float(base ** exponente)

# FUNCION CALCULAR RAIZ
def calcular_raiz(raiz: float, numero: float) -> float:
    resultado = None
    if raiz > 0:
        raiz =  float(1/raiz)
        resultado = elevar_potencia(numero, raiz)
    return resultado

# FUNCION CALCULAR DISCRIMINANTE
def calcular_discriminante(a, b, c):
    """
        El dicriminante se calcular como d = (b^2) - 4(a)(c)
    """
    disc = float(elevar_potencia(base = b, exponente = 2) - (4*a*c))
    return disc

def negativo(numero) -> float:
    return numero * -1

# CALCULAR INTERSECCIÓN CON EJE
def calcular_intersecion_con_eje(a, b, raiz_de_discriminante, raiz_disc_negativa: boolean):
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
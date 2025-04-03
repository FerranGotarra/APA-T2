# `esPrimo(numero)`   Devuelve `True` si su argumento es primo, y `False` si no lo es.
# `primos(numero)`    Devuelve una **tupla** con todos los números primos menores que su argumento.
# `descompon(numero)` Devuelve una **tupla** con la descomposición en factores primos de su argumento.
"""
Ferran Gotarra

"""
def esPrimo(numero):
    """"
    esPrimo determina si el numero introducido como parámetro es primo,
    donde retorna True, o False si no lo es.

    >>> esPrimo(4)
    False
    >>> esPrimo(-4)
    False
    """""
    for prova in range (2, numero):
        if numero % prova == 0:
            return False
    return True

def primos(numero):
    """
    Devuelve todos los números primos menores a numero.
        
    >>> primos (50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    return tuple(n for n in range(2, numero) if esPrimo(n))



def descompon(numero):
    """Devuelve un valor descompuesto en números primos.
    
    >>> descompon(36*175*143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    factores = []
    divisor = 2

    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    
    return tuple(factores)
def mcm(numero1, numero2):
    """Devuelve el mínimo común múltiplo de dos números.
    
    >>> mcm(90, 14)
    630
    """
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores_comunes = set(factores1) | set(factores2)
    resultado = 1
    for f in factores_comunes:
        resultado *= f ** max(factores1.count(f), factores2.count(f))
    return resultado

def mcd(numero1, numero2):
    """Devuelve el máximo común divisor de dos números.
    
    >>> mcd(924, 780)
    12
    """
    factores1 = descompon(numero1)
    factores2 = descompon(numero2)
    factores_comunes = set(factores1) & set(factores2)
    resultado = 1
    for f in factores_comunes:
        resultado *= f ** min(factores1.count(f), factores2.count(f))
    return resultado

def mcmN(*numeros):
    """Devuelve el mcm de varios argumentos.
    
    >>> mcmN(42, 60, 70, 63)
    1260
    """
    if not numeros: return 0
        
    resultado = numeros[0]
    for argumento in numeros[1:]:
        resultado = mcm(resultado, argumento)

    return resultado

def mcdN(*numeros):
    """Devuelve el mcd de varios argumentos.

    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    if not numeros: return 0
    
    resultado = numeros[0]
    for argumento in numeros[1:]:
        resultado = mcd(resultado, argumento)

    return resultado
    
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
import numpy as np
from random import randint
from os import system

def cantada_numeros():
        numero = []
        while len(numero) < 91:
            numero = np.random.choice(a = 91, size = 90, replace = False)
        return list(numero)

def cantar_numeros():
    print("")
    numero_cantado = cantada_numeros()
    return numero_cantado

def checkear_carton(carton, n_cantado):
    if any(isinstance(el, list) for el in carton):
        for i in carton:
            if n_cantado in i:
                index = i.index(n_cantado)
                i[index] = n_cantado * -1
        return carton
        
    else:
        carton_int = [int(i) for i in carton]

        if n_cantado in carton:
            index = carton.index(n_cantado)
            carton[index] = n_cantado * -1
            return carton
        else:
            return carton
        #carton_marcado = [n_carton * -1 for n_carton in carton if n_cantado == n_carton]
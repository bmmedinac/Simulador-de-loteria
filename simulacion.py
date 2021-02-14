import numpy as np
from random import randint
from os import system
from crea_numeros_carton import *
from cantar_checkear import *

def simular(cantidad_cartones = 1):
    
    # Preliminar
    loop = 1
    numero_cantado = list(np.random.choice(a = np.arange(1,91), size = 90, replace = False))
    
    # Crea la cantidad de cartones a simular
    cartones = []
    for i in list(range(0, cantidad_cartones)):
        if cantidad_cartones >= 2:
            solicitados = rellenar_numeros_columnas()
            cartones.append(solicitados)                
        else:
            cartones = rellenar_numeros_columnas()
        
    print(cartones) ### solo de checkeo
    
    while any(n > 0 for n in cartones) or loop > len(numero_cantado):
        p = checkear_carton(carton = cartones, n_cantado = numero_cantado.index(i))
        print(p)
        loop += 1
        
    if all(n < 0 for n in cartones):
        print("")
        print("LOTERIA! ¡Felicidades! Ganaste la lotería en " + str(loop) + " movimientos")
    
        
simular(cantidad_cartones = 1)



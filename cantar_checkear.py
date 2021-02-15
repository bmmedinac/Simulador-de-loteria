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
        #carton_int = [int(i) for i in carton]

        if n_cantado in carton:
            index = carton.index(n_cantado)
            carton[index] = n_cantado * -1
            return carton
        else:
            return carton

def conteo_polaridad(cartones):
        positivos, negativos = 0, 0
    
        if any(isinstance(el, list) for el in cartones):
            for num in cartones: 
                for c in num:
                # checking condition 
                    if c >= 0: 
                        positivos += 1
                        
                    else: 
                        negativos += 1
    
        elif len(cartones) == 15:
            for num in cartones: 
                # checking condition 
                    if num >= 0: 
                        positivos += 1
                        
                    else: 
                        negativos += 1
        
        return positivos, negativos

def tupleCounts2Percents(inputList):
    total = max(x[0] for x in inputList)
    return [(round((100 * x[0]/total), 1),
            round((100 * x[1]/total), 1)) for x in inputList]
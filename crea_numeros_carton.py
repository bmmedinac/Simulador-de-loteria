import numpy as np
from random import randint

def rellenar_numeros_columnas():
    numeros_totales = 0
    columna_no_vacia = True
    while numeros_totales != 15 and columna_no_vacia == True:
    # Asigna entre 1 a 3 números aleatorios en un rango a cada columna
        c1 = randint(1, 3)
        primera_columna = list(np.random.choice(a = range(1,9), size = c1, replace = False))
        
        c2 = randint(1, 3)
        segunda_columna = list(np.random.choice(a = range(10,19), size = c2, replace = False)) 
        
        c3 = randint(1, 3)
        tercera_columna = list(np.random.choice(a = range(20,29), size = c3, replace = False))
        
        c4 = randint(1, 3) 
        cuarta_columna = list(np.random.choice(a = range(30,39), size = c4, replace = False))
        
        c5 = randint(1, 3)
        quinta_columna = list(np.random.choice(a = range(40,49), size = c5, replace = False))
        
        c6 = randint(1, 3)
        sexta_columna = list(np.random.choice(a = range(50,59), size = c6, replace = False))
        
        c7 = randint(1, 3)
        septima_columna = list(np.random.choice(a = range(60,69), size = c7, replace = False))
        
        c8 = randint(1, 3)
        octava_columna = list(np.random.choice(a = range(70,79), size = c8, replace = False))
        
        c9 = randint(1, 3)
        novena_columna = list(np.random.choice(a = range(80,90), size = c9, replace = False))
        
        numeros_carton_particular = primera_columna + segunda_columna + tercera_columna + cuarta_columna + quinta_columna + sexta_columna + septima_columna + octava_columna + novena_columna
        # Registra la cantidad de números añadidos al cartón
        numeros_totales = int(c1) + int(c2) + int(c3) + int(c4) + int(c5) + int(c6) + int(c7) + int(c8) + int(c9)
        
        # Registra si existe al menos una columna con valor 0/Falso
        no_cero = [len(i) for i in [primera_columna, segunda_columna, tercera_columna, cuarta_columna, quinta_columna, sexta_columna, septima_columna, octava_columna, novena_columna]]
        columna_vacia = all(no_cero)
        
        if numeros_totales == 15 and columna_no_vacia == True:
            return list(numeros_carton_particular)
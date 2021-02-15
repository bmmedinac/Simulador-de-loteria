import numpy as np
from random import randint
from os import system
from crea_numeros_carton import *
from cantar_checkear import *
import matplotlib.pyplot as plt

class loteria():
    
    def __init__(self, negativos, positivos):
        self.negativos = negativos
        self.positivos = positivos
        
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
    
    def crear_cartones(cantidad_cartones = 1):
        
        # Crea la cantidad de cartones a simular
        cartones = []
        for i in list(range(1, cantidad_cartones + 1)):
            solicitados = rellenar_numeros_columnas()
            cartones.append(solicitados)
        
        return cartones
    
    def simular_numero_victorias(numeros_carton_elegido, primer_ganador = True):
        
        numero_cantado = list(np.random.choice(a = np.arange(1,91), size = 90, replace = False))
        loop = 1
        proporcion = []

        while any(i > 0 for n in numeros_carton_elegido for i in n) or loop <= 90:
            p = checkear_carton(carton = numeros_carton_elegido, n_cantado = numero_cantado.index(loop))
            loop += 1
            if primer_ganador == True:
                verdadero = next(all(c < 0 for c in casa) for casa in p)
                
                if verdadero == True:
                    print("El primer carton ganó en la cantada " + str(loop - 1) + " y los números: ")
                    print(p[verdadero])
                    break
                
            if primer_ganador == False:
                pos_neg = conteo_polaridad(p)
                proporcion.append(pos_neg)
                
        return proporcion
        
    def plot_proporcion(n):
        proporcion = loteria.simular_numero_victorias(loteria.crear_cartones(n), primer_ganador=False)
        progresion = tupleCounts2Percents(proporcion)
        x_axis = list(range(1, len(progresion) + 1))
        y_axis_positive = [x[0] for x in progresion]
        y_axis_negative = [x[1] for x in progresion]
        
        plt.plot(x_axis, y_axis_positive, label = "No marcado")
        plt.plot(x_axis, y_axis_negative, label = "Marcado")
        plt.ylabel('Proporción de números marcados')
        plt.xlabel('Iteración')
        plt.title('Progresión del marcado de números en ' + str(n) + " cartones")
        plt.xticks(np.arange(0, 91, 5))
        plt.legend()
        return plt.show()
        
#list(enumerate(proporcion)) ,
#print(loteria.crear_cartones(10))
#loteria.simular_numero_victorias(loteria.crear_cartones(2), primer_ganador=False)
#a = [1, 2, 4, 4]
#b = [-1, -2, -3, -4]
#c = [1, 2, -3, -4]
#d = [a, b, c]

loteria.plot_proporcion(100)
#n_cantado = list(np.random.choice(a = np.arange(1,91), size = 90, replace = False))
#checkear_carton(cartones, n_cantado)

#loteria.conteo_polaridad(loteria.crear_cartones())
#print(loteria.crear_cartones())


#polaridad = loteria.conteo_polaridad([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, -3])
#print(polaridad)
import numpy as np
from random import randint
from os import system
from crea_numeros_carton import *
from cantar_checkear import *
import matplotlib.pyplot as plt

class loteria():
    ####
    def cantada_numeros():
        numero = []
        while len(numero) < 91:
            numero = np.random.choice(a = 91, size = 90, replace = False)
        return list(numero)
    
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
    
    
    
    
    def simular_numero_victorias(numeros_carton_elegido, primer_ganador = True, agregado = True):
        
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
                if agregado == True:
                    pos_neg = conteo_polaridad(p)
                    proporcion.append(pos_neg)
                
                if agregado == False:
                    pos_neg = [conteo_polaridad(x) for x in p]
                    proporcion.append(pos_neg)
                
        return proporcion
        
        
        
    class simular():   
        
        def __init__(self, general = True): 
        # create a inner class object 
            #self.proporcion = proporcion
            self.general = general
        
        def proporcion(n, general = True):
            if general == True:
                proporcion = loteria.simular_numero_victorias(loteria.crear_cartones(n), primer_ganador=False, agregado = True)
                progresion = tupleCounts2Percents(proporcion)
                return progresion
            
            if general == False:
                num = limit(n)
                num = 5
                proporcion = loteria.simular_numero_victorias(loteria.crear_cartones(num), primer_ganador=False, agregado = False)
                rotated = list(zip(*proporcion))
                progresion = [tupleCounts2Percents(x) for x in rotated]
            
                return progresion
        
        def plot(progresion, general = True):
            
            if general == True:
                x_axis = list(range(1, 91))
                y_axis_positive = [x[0] for x in progresion]
                y_axis_negative = [x[1] for x in progresion]
                
                plt.plot(x_axis, y_axis_positive, label = "No marcado")
                plt.plot(x_axis, y_axis_negative, label = "Marcado")
                plt.ylabel('Proporción de números marcados')
                plt.xlabel('Iteración')
                plt.title("Progresión del marcado de números en cartones")
                plt.xticks(np.arange(0, 91, 5))
                plt.legend()
                return plt.show()
            
            if general == False:
                x_axis = list(range(1, 91))
                y_axis_positive0 = [x[1] for x in progresion[0]]
                y_axis_positive1 = [x[1] for x in progresion[1]]
                y_axis_positive2 = [x[1] for x in progresion[2]]
                y_axis_positive3 = [x[1] for x in progresion[3]]
                y_axis_positive4 = [x[1] for x in progresion[4]]
                #y0 = progresion[0][78][0]
                plt.plot(x_axis, y_axis_positive0, label = "Cartón 1")
                plt.plot(x_axis, y_axis_positive1, label = "Cartón 2")
                plt.plot(x_axis, y_axis_positive2, label = "Cartón 3")
                plt.plot(x_axis, y_axis_positive3, label = "Cartón 4")
                plt.plot(x_axis, y_axis_positive4, label = "Cartón 5")
                plt.ylabel('Proporción de números marcados')
                plt.xlabel('Iteración')
                plt.title("Progresión del marcado de números en cartones")
                plt.xticks(np.arange(0, 91, 5))
                plt.legend()
                return plt.show()
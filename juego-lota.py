##### HEAD ######

import numpy as np
from random import randint
from os import system
from crea_numeros_carton import *
from cantar_checkear import *

programa_titulo = "Loteria - tu lota de la playa"
system("mode 110, 30")
system("Título: " + programa_titulo)

def clear():
    system('clear')
    
####### INICIO DEL JUEGO ####
clear()
print("Lotería - Tu lota de la playa")

def intro():
    print("")
    print("¡Pase, caserita, caserito! ¡Juéguese una lota!")
    print("¡Llévese un microondas, unas papitas pa' picar, todo con su lota!")
    print("")
    print("Tóme, un cartón de cortesia de la casa, porque me cayó bien...")
    input("Aprieta Enter para recibir el cartón que te regaló el buen hombre...")

intro()

print("Estamos en la playa, pero la tecnología no falta. Los números de tu cartón se generan automáticamente.")
input("Aprieta Enter para generar un cartón.")

numeros_carton_elegido = None

def crear_carton():
    global numeros_carton_elegido
    clear()
    print("¿Te gusta estos números?")
    print("")
    oferta_numeros = rellenar_numeros_columnas()
    print(oferta_numeros)
    print("")
    
    while numeros_carton_elegido is None:
        eleccion_carton = input("""
        
        Si te gustaron estos números, presiona 1. Si quieres otro cartón, presiona 2. Si quieres irte, presiona 0
                                
        > """)
        if eleccion_carton == "1":
            clear()
            print("¡A JUGAR! Tus números son:")
            numeros_carton_elegido = oferta_numeros
            print(numeros_carton_elegido)
        elif eleccion_carton == "2":
            clear()
            print("¿Y este cartón?")
            print("")
            oferta_numeros = rellenar_numeros_columnas()
            print(oferta_numeros)
        elif eleccion_carton == "0":
            clear()
            print("¡Vuelve pronto!")
            break
        else:
            print("Ingresa una opción válida")

crear_carton()

clear()
print("¡¡Qué empiece la lota!!")
print("Si tienes un número que salga, este se marcará con un '-'. Por ejemplo, si sale el 1, se marcará como '-1':")
print("")
input("Presiona Enter para sacar el primer número...")


numero_cantado = list(np.random.choice(a = np.arange(1,91), size = 90, replace = False))

def juego_loteria():
    i = 1
    while any(n > 0 for n in numeros_carton_elegido) or i > len(numero_cantado):
        print(i)
        print("En esta tirada el numerito es el " + str(numero_cantado.index(i)))
        print("")
        p = checkear_carton(carton = numeros_carton_elegido, n_cantado = numero_cantado.index(i))
        print(p)
        print("")
        proceso_jugador = input("""Presiona Enter para sacar otro número, o 0 si deseas dejar de jugar
                                
                                >  """)
        i += 1
        if proceso_jugador == "0":
            clear()
            print("¡Vuelve pronto!")
            break
        
        elif all(numeros_carton_elegido) < 0:
            print("")
            print("LOTERIA! ¡Felicidades! Ganaste la lotería en " + str(i) + " movimientos")
        
        else:
            clear()
            continue
        
    if all(n < 0 for n in numeros_carton_elegido):
        print("")
        print("LOTERIA! ¡Felicidades! Ganaste la lotería en " + str(i) + " movimientos")
        
    
juego_loteria()
# -*- coding: utf-8 -*-
"""
@author: Giancarlo Culcay
"""

import random
import os

IMAGES = ['''           
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        |
    =========''']

palabras = []
intentos = 7
aciertos= 0
errores = 0
z = 0

def normalizar(s): # Quita tildes
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

def palabra_random():
    with open("./archivos/data.txt","r", encoding="utf-8") as fichero:
        for linea in fichero:
            linea_formateada = linea.replace("\n","")
            palabras.append(linea_formateada)
    return normalizar((random.choice(palabras)))


def presentacion():
    os.system ("cls") 
    texto_inicial = " Juego del Ahorcado "
    texto_presentar = texto_inicial.center(50,'-') 
    print(texto_presentar,"\n")
    print("=> Adivina la palabra :")
    print(IMAGES[errores])
    f_mostrar(palabra_oculta)
    print("intentos: ",intentos)
    print("aciertos: ",aciertos)
    print("errores:  ",errores)

def f_mostrar(x):
    mostrar = "".join(x) 
    print(mostrar,'\n')

def verificar(letra):
    if len(letra) == 0 and letra.isalpha() :
        errores +=1

os.system ("cls") 
palabra = palabra_random()
palabra_oculta = ["_"]*len(palabra)


while True:
    try:
        presentacion()
        #print(palabra)   #respuesta, comentar o eliminar
        l = input("Ingresa una letra: ")
        verificar(l)

        if l in palabra_oculta :
            errores +=1
            print("Ya ingresaste esta letra")
        else:
            for index,x in enumerate(palabra):
                if x == l:
                    palabra_oculta[index] = l
                    aciertos += 1

        if palabra.find(l) == -1:   #sino encuentra, devuelve -1
            errores +=1

        f_mostrar(palabra_oculta)
        presentacion()
        mipalabra = "".join(palabra_oculta)  
        
        if errores >= intentos:
            print("Has perdido :(")
            print(f'La palabra era: {palabra}')
            break

        if mipalabra == palabra :
            print("""
   _____          _   _           _____ _______ ______ 
  / ____|   /\   | \ | |   /\    / ____|__   __|  ____|
 | |  __   /  \  |  \| |  /  \  | (___    | |  | |__   
 | | |_ | / /\ \ | . ` | / /\ \  \___ \   | |  |  __|  
 | |__| |/ ____ \| |\  |/ ____ \ ____) |  | |  | |____ 
  \_____/_/    \_\_| \_/_/    \_\_____/   |_|  |______|
                                                                                                          
        """)
            print("Felicidades Ganaste!! :D")
            break

    except ValueError:
        print("Porfavor ingresa solo una letra")
        #print("Ya has ingresado!")
    except IndexError:
        print("Fin")
 

from principal import *
from configuracion import *
import random
import math


def nuevaPalabra(lista):
    a = lista[random.randint(0, len(lista))]
    return a


def lectura(archivo, salida, largo):
    lemario = archivo.readlines()
    for i in lemario:
        if len(i) == largo+1:
            salida.append(i) 
    return salida


def revision(palabraCorrecta, palabra, correctas, incorrectas, casi):
    if palabra == palabraCorrecta:
        return True
    for k in range(len(palabra)):
        a = True
        for i in range(len(palabraCorrecta)):
            if palabra[k] == palabraCorrecta[i]:
                a = False
                if k == i:
                    correctas.append(palabra[i])
                else:
                    casi.append(palabra[k])
        if a:
            incorrectas.append(palabra[k])
    else:
        return False

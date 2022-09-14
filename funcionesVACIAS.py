from principal import *
from configuracion import *
import random
import math
import pygame
####random1 = ....
##ramdom2 = ....
##
##validar que ramdom2 no sea igual a random1 y random1 + 1
##sino volver hacer ramdom2
##
##agegar a la lista ( subtitulo en la posicion ramdom1 )
##agegar a la lista ( subtitulo en la posicion ramdom1 +1 )
##agegar a la lista ( subtitulo en la posicion ramdom2 )
##
##retornar lista

def lectura(archivo, subtitulo,n):

    for line in archivo:#PREGUNTO PARA LA LINEA EN EL ARCHIVO
     if not line.startswith(('0', '1' , '2', '3',"4","5","6","7","8","9","\n")):#ACA DIGO SI LA LINEA NO COMIENZA CON...
      subtitulo.append(line.replace("<i>","").replace("ñ","ni").replace("¡","").replace("¿","").replace("...","").replace("\n","").replace("-","").replace("</i>","").replace('"',"").lower())
        #ACA LOS APENDEO Y REEPLAZO CARACTERES PARA UNA MEJOR LECTURA


    #se queda solo con los subtitulo de cierta longitud y filtra
    #subtitulo.append("Hola")

def seleccion(subtitulo):
    print (len(subtitulo))
    lista=[]
    r1=random.randint(0,len(subtitulo)-2)#ES PARA QUE ME DE ENTRE 0 Y EL ANTEULTIMO SUBTITULO,PORQUE DESPUES LE SUMO 1.
    r2=random.randint(0,len(subtitulo)-1)#ES MENOS UNO PORQUE SOLO TOMA UNO Y NO EL SIGUIENTE
    #PASARLO A WHILE
    while r2 ==r1 or r2==r1+1:#MIENTRAS SEAN IGUALES VOLVERA A BUSCAR UN RANDOM, PARA QUE NO SE REPITA EL PRIMERO Y EL SIGUIENTE
        r2=random.randint(0,len(subtitulo)-1)
    lista.append(subtitulo[r1])#APENDEO
    lista.append(subtitulo [r1+1])#APENDEO EL SIGUIENTE
    lista.append(subtitulo[r2])#APENDEO CUALQUIER OTRO RANDOM
    return lista #RETORNO LISTA DE 3 SUBTITULOS APENDEADOS

#elige uno al azar, lo devuelve, el siguiente y otro
   # lista=["no se llama mas puerco arania","de ahora en mas es puerco potter", "epa epa epa epaaaa"]
    #return lista

def puntos(n):
    if n <0: #SI EL PARAMETRO ES MENOR A CERO, NO SUMA NADA
        return 0
    else:
        return 2*n #AGARRA EL PUNTAJE DE LA CANTIDAD DE ACIERTOS SEGUIDOS *2

    #devuelve el puntaje, segun seguidilla


def procesar(palabraUsuario, mostrada,siguiente, otra, correctas):

    nuevoPuntaje=0
    if siguiente.startswith(palabraUsuario) :#pregunto si empieza con las letras y si no esta vacia la string, SI ES VERDADERO SUMA UNA CORRECTA
        var=correctas+1

        nuevoPuntaje = puntos(correctas+1)#me suma puntaje
        reproson("perfecti.wav") #REPRODUCE SONIDO

    else:
        nuevoPuntaje = -3 #puntos(correctas-3)
        var1=correctas-1 #sino me resta

        reproson("jaja.wav")
    return nuevoPuntaje #retorna puntaje

    #chequea que sea correcta, que pertenece solo a la frase siguiente. Devuelve puntaje segun seguidilla

def reproson (nombresonido): #creo funcion para reproducir sonidos

    effect = pygame.mixer.Sound(nombresonido)
    effect.play()


def dibujarpantallafinal (screen,puntos):

    defaultFontGrande= pygame.font.SysFont( "Tahoma",TAMANNO_LETRA_GRANDE)

##    screen.blit(defaultFontGrande.render("EL JUEGO TERMINO", 1, COLOR_TEXTO), (300, 10))
    screen.blit(defaultFontGrande.render("" + str(puntos), 1, COLOR_LETRAS), (390, 425))
    reproson ("finalis.mp3")



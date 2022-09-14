#! /usr/bin/env python
import os, random, sys, math

import pygame
from pygame.locals import *
from configuracion import *
from extras import *

from funcionesVACIAS import *

#Funcion principal
def main():
        #Centrar la ventana y despues inicializar pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()
        #pygame.mixer.init()
        #pantalla=pygame.display.set_mode(ANCHO,ALTO)
        #Preparar la ventana
        pygame.display.set_caption("Los Simpsons: The Game")
        screen = pygame.display.set_mode((ANCHO, ALTO))
        pygame.mixer.music.load("Simpsons_Intro2.mp3")# CARGO MUSICA DE FONDO
        pygame.mixer.music.play(-1)#EL MENOS UNO ES PARA QUE CORRA INFINITAMENTE
        #tiempo total del juego
        gameClock = pygame.time.Clock()
        totaltime = 0
        segundos = TIEMPO_MAX
        fps = FPS_inicial


        puntos = 0
        palabraUsuario = ""

        subtitulo=[]
        correctas=0

        archivo= open("TheSimpsons.txt","r")

        #lectura del archivo y filtrado de caracteres especiales


        lectura(archivo, subtitulo, N)

        #elige unsubtitulo al azar, su siguiente y otro
        lista=seleccion(subtitulo)

        print(lista)
        azar=random.randrange(2)
        dibujar(screen, palabraUsuario, lista, azar, puntos, segundos)

        IMA= pygame.image.load("over.JPg").convert()#CARGO IMAGENES A USAR EN EL PROGRAMA
        background_image = pygame.image.load("fondo0.JPG").convert()#CARGO IMAGENES A SAR EN EL PROGRAMA
        while segundos > fps/1000:

        # 1 frame cada 1/fps segundos
            gameClock.tick(fps)
            totaltime += gameClock.get_time()


            if True:
            	fps = 3

            #Buscar la tecla apretada del modulo de eventos de pygame
            for e in pygame.event.get():

                #QUIT es apretar la X en la ventana
                if e.type == QUIT:
                    pygame.quit()
                    return()

                #Ver si fue apretada alguna tecla
                if e.type == KEYDOWN:
                    letra = dameLetraApretada(e.key)
                    palabraUsuario += letra
                    if e.key == K_BACKSPACE:
                        palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                    if e.key == K_RETURN:
                        #chequea si es correcta y suma o resta puntos
                        if palabraUsuario!="":
                            sumar=procesar(palabraUsuario, lista[0], lista[1], lista[2],correctas)
                            puntos+=sumar
                            if sumar>0:
                                correctas=correctas+1
                            else:
                                correctas=0

                            #elige un subtitulo al azar, su siguiente y otro
                            lista=seleccion(subtitulo)
                            palabraUsuario = ""
                            #cambia el orden al azar
                            azar=random.randrange(2)


            segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

            #Limpiar pantalla anterior
            screen.fill(COLOR_FONDO)

            #Dibujar de nuevo todo
            screen.blit(background_image, [0, 0])
            dibujar(screen, palabraUsuario, lista, azar, puntos, segundos)




            pygame.display.flip()




        screen.blit(IMA, [0, 0]) #cargo la imagen

        dibujarpantallafinal(screen,puntos)#dibujo la imagen con los puntos finales
        pygame.display.flip()

        while 1:
            #Esperar el QUIT del usuario

            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return

        archivo.close()

#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()

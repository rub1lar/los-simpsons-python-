import pygame
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")


def dibujar(screen, palabraUsuario, lista, azar, puntos, segundos):


    defaultFont= pygame.font.SysFont( "SimpsonFont", TAMANNO_LETRA)
    defaultFontGrande= pygame.font.SysFont( "SimpsonFont",30)#el tamaño y tipo de letra

    #Linea Horizontal
    pygame.draw.line(screen, (0,0,0), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFontGrande.render(palabraUsuario, 1, COLOR_USUARIO), (240, 540))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 1))
    #muestra los segundos y puede cambiar de color con el tiempo
    if(segundos<15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 1))

    #muestra el nombre de la Peli
    #screen.blit(defaultFont.render("The Simpsons", 1, COLOR_PELI), (ANCHO//2-len("The Simpsons")*TAMANNO_LETRA//4,(TAMANNO_LETRA)))
##    screen.blit(defaultFontGrande.render("The Simpsons", 1, COLOR_PELI), (ANCHO//2-len("The Simpsons")*TAMANNO_LETRA_GRANDE//4,(TAMANNO_LETRA*2)))
    #muestra los subtitulos
    screen.blit(defaultFontGrande.render(lista[0], 1, COLOR_TEXTO), (ANCHO//2-len(lista[0])*TAMANNO_LETRA_GRANDE//4,(TAMANNO_LETRA_GRANDE)*6))
    if azar==0:
        screen.blit(defaultFontGrande.render(lista[1], 1, COLOR_LETRAS), (ANCHO//2-len(lista[1])*TAMANNO_LETRA_GRANDE//4,(TAMANNO_LETRA_GRANDE)*8))
        screen.blit(defaultFontGrande.render(lista[2], 1, COLOR_LETRAS), (ANCHO//2-len(lista[2])*TAMANNO_LETRA_GRANDE//4,(TAMANNO_LETRA_GRANDE)*10))
    else:
        screen.blit(defaultFontGrande.render(lista[2], 1, COLOR_LETRAS), (ANCHO//2-len(lista[2])*TAMANNO_LETRA_GRANDE//4,(TAMANNO_LETRA_GRANDE)*8))
        screen.blit(defaultFontGrande.render(lista[1], 1, COLOR_LETRAS), (ANCHO//2-len(lista[1])*TAMANNO_LETRA_GRANDE//4,(TAMANNO_LETRA_GRANDE)*10))



#def dibujarpantallainicial (screen):

    #defaultFontGrande= pygame.font.SysFont( "Simpsonfont",TAMANNO_LETRA_GRANDE)

##    screen.blit(defaultFontGrande.render("EL JUEGO TERMINO", 1, COLOR_TEXTO), (300, 10))
    #screen.blit(defaultFontGrande.render("" + str(puntos), 1, COLOR_USUARIO), (390, 440))


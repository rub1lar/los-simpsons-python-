def filtrado (caracter,cadena):
    nueva=""
    for elem in cadena:
        if elem!=caracter:
            nueva=nueva+elem
    return nueva

archivo=open("TheSimpsons.txt","r")
subtitulo=[]
cont=0
while cont<=3:
    for line in archivo:
     if not line.startswith(('0', '1' , '2', '3',"4","5","6","7","8","9")):
        cont=cont+1
        subtitulo.append(line)



print (subtitulo)

###print (a,lista)



#cerramos el archivo
archivo.close()

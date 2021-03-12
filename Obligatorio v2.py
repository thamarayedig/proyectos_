def Menu():
    título = "JUEGO:"                                   #Asigno para después centrarla
    título2 = "4 EN LÍNEA"
    print(título.center(50,"-"))
    print(título2.center(50,"-"))
    print("")
    print(" 1- Instrucciones","\n","2- Jugar","\n","3- Contacto con responsables")
    Opciones=1
    while (Opciones!=0):
        Opciones= int(input(" Ingrese su elección : "))
        if Opciones == 1:
            print("")
            print(" Instrucciones:")
            print(" Digitar el número de columna y presionar 'Enter',la ficha se ubicará en la última fila libre.")
            print(" -------------")
        elif(Opciones == 2):
            print("")
            print(" La partida comenzará")
            print(" -------------")
            Comienzo = Start()                          #Asigno para llamar a la función
            Comienzo
            break

        elif(Opciones == 3):
            print("")
            print(" Thamara Yedig,098 835 892 ; Joaquín Machado, 091 848 599")
            print(" -------------")
        else:
            print("")
            print(" Ingresó un caracter inválido")
            
            
def MostrarTablero(lista):
    tablero = ""
    contador = 0
    for i in lista:
        if (contador == 14):
            tablero += i + "\n"
            contador = 0
        else:
            tablero += i
            contador += 1
    print(tablero)

def CrearTablero():
        lista = ["|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|",
             "|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"," ","|"]
        return lista

def Start():
    J1=input("Ingrese su nombre jugador 1: ")
    J2=input("Ingrese su nombre jugador 2: ")
    tablero = CrearTablero()
    victoria = False
    columna = False
    contador = 0
    tablero_index = {1: 76, 2: 78, 3: 80, 4: 82, 5: 84, 6: 86, 7: 88} #Número de columna: Índice.
    print("La ficha de ", J1, " es X ")
    print("La ficha de ", J2, " es O ") 
    


    while (victoria == False):
        columna = False

###JUGADOR 1
        if ((contador % 2) == 0):                           #Para saber turno.

            while True:                                     #Prueba los datos que se ingresan, si existe un error lo detecta y lo informa.
                try:
                    print(J1,end=" ")
                    elegir=int(input("Ingrese un número(del 1 al 7) de columna donde jugar :"))
                    if (0< elegir <=7):
                        break
                    else:
                        print("Número fuera del rango")
                except ValueError:
                    print("Ingresó un caracter érroneo")
            
            
                
            
                
            if (elegir in tablero_index):                   #Para saber si la columna ingresada es válida.
                contador_columna = tablero_index[elegir]
                
                while (columna == False):   
                    
                    if (tablero[contador_columna] != " "):  #Se fija si la posicion deseada está ocupada.
                        contador_columna -= 15              #Si la posición está ocupada,contador_columna vale 15 posiciones menos y se vuelve a repetir el código.
                        while contador_columna<0:           #Si contador_columna es negativo no queda lugar en la colummna.
                        
                            print("La columna está llena")
                            print(J1,end=" ")
                            elegir = int(input(":porfavor ingrese otra columna desea colocar: "))
                            contador_columna=tablero_index[elegir]  #Vuelve a tomar el valor para ver si se vuelve a cumplir el while.
                            
                                
                                
                    else:                                   #Si la posicion está libre.
                        tablero[contador_columna] = "X"     #Se sustituye por la ficha
                        contador += 1                       #Aumenta 1 al contador para cambiar de turno.
                        columna = True                      #Para terminar con el bucle.
                        if (Victoria(tablero) == True):     #Si se cumple una condición de victoria .
                            victoria = True                 #Termina el juego al salir del bucle
                            MostrarTablero(tablero)
                            print(J1," ganó!!!")
                            exit()
                        else:                               #Para continuar jugando si no se cumple la victoria
                            MostrarTablero(tablero)
            


###JUGADOR 2
        else:
        
            while True:                                     #Prueba los datos que se ingresan, si existe un error lo detecta y lo informa.
                try:
                    print(J2,end=" ")
                    elegir=int(input("Ingrese un número(del 1 al 7) de columna donde jugar :"))
                    if (0< elegir <=7):
                        break
                    else:
                        print("Número fuera del rango")
                        
                except ValueError:
                    print("Ingresó un caracter érroneo")
            


            if (elegir in tablero_index):                   #Para encontrar la posición de la ficha.
                contador_columna = tablero_index[elegir]

                while (columna == False):
                    if (tablero[contador_columna] != " "):  #Se fija si la posicion deseada esta ocupada.  
                        contador_columna -= 15              #Si la posición está ocupada,contador_columna vale 15 posiciones menos y se vuelve a repetir el código.
                        while contador_columna<0:           #Si contador_columna es negativo no queda lugar en la colummna.
                        
                            print("La columna está llena")
                            print(J2,end=" ")
                            elegir = int(input(": porfavor ingrese otra columna desea colocar: "))
                            contador_columna=tablero_index[elegir]  #Vuelve a tomar el valor para ver si se vuelve a cumplir el while.
                    else:                                   #Si la posicion está libre.
                        tablero[contador_columna] = "O"     #Se sustituye por la ficha.
                        contador += 1                       #Aumenta 1 al contador para cambiar de turno.
                        columna = True                      #Para terminar con el bucle.
                        if (Victoria(tablero)):             #Si se cumple una condición de victoria.
                            victoria = True                 #Termina el juego al salir del bucle
                            
                            MostrarTablero(tablero)
                            print(J2," ganó!!!")
                            exit()
                        else:
                            MostrarTablero(tablero)
        
        
            


def Victoria(lista_tablero):

    #Condiciones para ganar verticalmente desde la fila 1 hasta la fila 4.
    
    #1 COLUMNA VERTICAL
    if ((lista_tablero[1] == "X" and lista_tablero[16] == "X" and lista_tablero[31] == "X" and
        lista_tablero[46] == "X") or (lista_tablero[1] == "O" and lista_tablero[16] == "O" and
        lista_tablero[31] == "O" and lista_tablero[46] == "O")):
        return True
        
    #2 COLUMNA VERTICAL
    if ((lista_tablero[3] == "X" and lista_tablero[18] == "X" and lista_tablero[33] == "X" and
        lista_tablero[48] == "X") or (lista_tablero[3] == "O" and lista_tablero[18] == "O" and
        lista_tablero[33] == "O" and lista_tablero[48] == "O")):
        return True
    #3 COLUMNA VERTICAL
    if ((lista_tablero[5] == "X" and lista_tablero[20] == "X" and lista_tablero[35] == "X" and
        lista_tablero[50] == "X") or (lista_tablero[5] == "O" and lista_tablero[20] == "O" and
        lista_tablero[35] == "O" and lista_tablero[50] == "O")):
        return True
    #4 COLUMNA VERTICAL
    if ((lista_tablero[7] == "X" and lista_tablero[22] == "X" and lista_tablero[37] == "X" and
        lista_tablero[52] == "X") or (lista_tablero[7] == "O" and lista_tablero[22] == "O" and
        lista_tablero[37] == "O" and lista_tablero[52] == "O")):
        return True
    #5 COLUMNA VERTICAL
    if ((lista_tablero[9] == "X" and lista_tablero[24] == "X" and lista_tablero[39] == "X" and
        lista_tablero[54] == "X") or (lista_tablero[9] == "O" and lista_tablero[24] == "O" and
        lista_tablero[39] == "O" and lista_tablero[54] == "O")):
        return True
    #6 COLUMNA VERTICAL
    if ((lista_tablero[11] == "X" and lista_tablero[26] == "X" and lista_tablero[41] == "X" and
        lista_tablero[56] == "X") or (lista_tablero[11] == "O" and lista_tablero[26] == "O" and
        lista_tablero[41] == "O" and lista_tablero[56] == "O")):
        return True
    #7 COLUMNA VERTICAL
    if ((lista_tablero[13] == "X" and lista_tablero[28] == "X" and lista_tablero[43] == "X" and
        lista_tablero[58] == "X") or (lista_tablero[13] == "O" and lista_tablero[28] == "O" and
        lista_tablero[43] == "O" and lista_tablero[58] == "O")):
        return True


    ##Condiciones para ganar verticalmente desde la fila 2 hasta la fila 5
    #1 COLUMNA VERTICAL
    if ((lista_tablero[16] == "X" and lista_tablero[31] == "X" and lista_tablero[46] == "X" and
        lista_tablero[61] == "X") or (lista_tablero[16] == "O" and lista_tablero[31] == "O" and
        lista_tablero[46] == "O" and lista_tablero[61] == "O")):
        return True
    #2 COLUMNA VERTICAL
    if ((lista_tablero[18] == "X" and lista_tablero[33] == "X" and lista_tablero[48] == "X" and
        lista_tablero[63] == "X") or (lista_tablero[18] == "O" and lista_tablero[33] == "O" and
        lista_tablero[48] == "O" and lista_tablero[63] == "O")):
        return True
    #3 COLUMNA VERTICAL
    if ((lista_tablero[20] == "X" and lista_tablero[35] == "X" and lista_tablero[50] == "X" and
        lista_tablero[65] == "X") or (lista_tablero[20] == "O" and lista_tablero[35] == "O" and
        lista_tablero[50] == "O" and lista_tablero[65] == "O")):
        return True
    #4 COLUMNA VERTICAL
    if ((lista_tablero[22] == "X" and lista_tablero[37] == "X" and lista_tablero[52] == "X" and
        lista_tablero[67] == "X") or (lista_tablero[22] == "O" and lista_tablero[37] == "O" and
        lista_tablero[52] == "O" and lista_tablero[67] == "O")):
        return True
    #5 COLUMNA VERTICAL
    if ((lista_tablero[24] == "X" and lista_tablero[39] == "X" and lista_tablero[54] == "X" and
        lista_tablero[69] == "X") or (lista_tablero[24] == "O" and lista_tablero[39] == "O" and
        lista_tablero[54] == "O" and lista_tablero[69] == "O")):
        return True
    #6 COLUMNA VERTICAL
    if ((lista_tablero[26] == "X" and lista_tablero[41] == "X" and lista_tablero[56] == "X" and
        lista_tablero[71] == "X") or (lista_tablero[26] == "O" and lista_tablero[41] == "O" and
        lista_tablero[56] == "O" and lista_tablero[71] == "O")):
        return True
    #7 COLUMNA VERTICAL
    if ((lista_tablero[28] == "X" and lista_tablero[43] == "X" and lista_tablero[58] == "X" and
        lista_tablero[73] == "X") or (lista_tablero[28] == "O" and lista_tablero[43] == "O" and
        lista_tablero[58] == "O" and lista_tablero[73] == "O")):
        return True



       #Condiciones para ganar verticalmente desde la fila 3 hasta la fila 6.
    #1 COLUMNA VERTICAL
    if ((lista_tablero[31] == "X" and lista_tablero[46] == "X" and lista_tablero[61] == "X" and
        lista_tablero[76] == "X") or (lista_tablero[31] == "O" and lista_tablero[46] == "O" and
        lista_tablero[61] == "O" and lista_tablero[76] == "O")):
        return True
    #2 COLUMNA VERTICAL
    if ((lista_tablero[33] == "X" and lista_tablero[48] == "X" and lista_tablero[63] == "X" and
        lista_tablero[78] == "X") or (lista_tablero[33] == "O" and lista_tablero[48] == "O" and
        lista_tablero[63] == "O" and lista_tablero[78] == "O")):
        return True
    #3 COLUMNA VERTICAL
    if ((lista_tablero[35] == "X" and lista_tablero[50] == "X" and lista_tablero[65] == "X" and
        lista_tablero[80] == "X") or (lista_tablero[35] == "O" and lista_tablero[50] == "O" and
        lista_tablero[65] == "O" and lista_tablero[80] == "O")):
        return True
    #4 COLUMNA VERTICAL
    if ((lista_tablero[37] == "X" and lista_tablero[52] == "X" and lista_tablero[67] == "X" and
        lista_tablero[82] == "X") or (lista_tablero[37] == "O" and lista_tablero[52] == "O" and
        lista_tablero[67] == "O" and lista_tablero[82] == "O")):
        return True
    #5 COLUMNA VERTICAL
    if ((lista_tablero[39] == "X" and lista_tablero[54] == "X" and lista_tablero[69] == "X" and
        lista_tablero[84] == "X") or (lista_tablero[39] == "O" and lista_tablero[54] == "O" and
        lista_tablero[69] == "O" and lista_tablero[84] == "O")):
        return True
    #6 COLUMNA VERTICAL
    if ((lista_tablero[41] == "X" and lista_tablero[56] == "X" and lista_tablero[71] == "X" and
        lista_tablero[86] == "X") or (lista_tablero[41] == "O" and lista_tablero[56] == "O" and
        lista_tablero[71] == "O" and lista_tablero[86] == "O")):
        return True
    #7 COLUMNA VERTICAL
    if ((lista_tablero[43] == "X" and lista_tablero[58] == "X" and lista_tablero[73] == "X" and
        lista_tablero[88] == "X") or (lista_tablero[43] == "O" and lista_tablero[58] == "O" and
        lista_tablero[73] == "O" and lista_tablero[88] == "O")):
        return True

    #DIAGONALES
       #Del 82 A 76
    #1  Diagonal con 1 posibilidad
    if ((lista_tablero[82] == "X" and lista_tablero[69] == "X" and lista_tablero[56] == "X" and
        lista_tablero[43] == "X") or (lista_tablero[82] == "O" and lista_tablero[69] == "O" and
        lista_tablero[56] == "O" and lista_tablero[43] == "O")):
        return True
    #2 Diagonal con 2 posibilidades
    if ((lista_tablero[80] == "X" and lista_tablero[67] == "X" and lista_tablero[54] == "X" and
        lista_tablero[41] == "X") or (lista_tablero[80] == "O" and lista_tablero[67] == "O" and
        lista_tablero[54] == "O" and lista_tablero[41] == "O")):
        return True
    if ((lista_tablero[67] == "X" and lista_tablero[54] == "X" and lista_tablero[41] == "X" and
        lista_tablero[28]=="X" ) or (lista_tablero[67] == "O" and lista_tablero[54] == "O" and
        lista_tablero[41]and lista_tablero[28] == "O")):
        return True

    
    #3 Diagonal con 3 posibilidades
    if ((lista_tablero[78] == "X" and lista_tablero[65] == "X" and lista_tablero[52] == "X" and
        lista_tablero[39] == "X") or (lista_tablero[78] == "O" and lista_tablero[65] == "O" and
        lista_tablero[52] == "O" and lista_tablero[39] == "O")):
        return True
    if ((lista_tablero[26] == "X" and lista_tablero[65] == "X" and lista_tablero[52] == "X" and
        lista_tablero[39] == "X") or (lista_tablero[26] == "O" and lista_tablero[65] == "O" and
        lista_tablero[52] == "O" and lista_tablero[39] == "O")):
        return True
    if ((lista_tablero[26] == "X" and lista_tablero[13] == "X" and lista_tablero[52] == "X" and
        lista_tablero[39] == "X") or (lista_tablero[26] == "O" and lista_tablero[13] == "O" and
        lista_tablero[52] == "O" and lista_tablero[39] == "O")):
        return True
    
    #4 Diagonal con 3 posibilidades
    if ((lista_tablero[76] == "X" and lista_tablero[63] == "X" and lista_tablero[50] == "X" and
        lista_tablero[37] == "X") or (lista_tablero[76] == "O" and lista_tablero[63] == "O" and
        lista_tablero[50] == "O" and lista_tablero[37] == "O")):
        return True
    if ((lista_tablero[24] == "X" and lista_tablero[63] == "X" and lista_tablero[50] == "X" and
        lista_tablero[37] == "X") or (lista_tablero[24] == "O" and lista_tablero[63] == "O" and
        lista_tablero[50] == "O" and lista_tablero[37] == "O")):
        return True
    if ((lista_tablero[24] == "X" and lista_tablero[11] == "X" and lista_tablero[50] == "X" and
        lista_tablero[37] == "X") or (lista_tablero[24] == "O" and lista_tablero[11] == "O" and
        lista_tablero[50] == "O" and lista_tablero[37] == "O")):
        return True
    
    #5 Diagonal con 2 posibilidades
    if ((lista_tablero[61] == "X" and lista_tablero[48] == "X" and lista_tablero[35] == "X" and
        lista_tablero[22] == "X") or (lista_tablero[61] == "O" and lista_tablero[48] == "O" and
        lista_tablero[35] == "O" and lista_tablero[22] == "O")):
        return True
    if ((lista_tablero[9] == "X" and lista_tablero[48] == "X" and lista_tablero[35] == "X" and
        lista_tablero[22] == "X") or (lista_tablero[9] == "O" and lista_tablero[48] == "O" and
        lista_tablero[35] == "O" and lista_tablero[22] == "O")):
        return True
    #6 Diagonal con 1 posibilidad
    if ((lista_tablero[46] == "X" and lista_tablero[33] == "X" and lista_tablero[20] == "X" and
        lista_tablero[7] == "X") or (lista_tablero[46] == "O" and lista_tablero[33] == "O" and
        lista_tablero[20] == "O" and lista_tablero[7] == "O")):
        return True

    #DIAGONAL

    #Fila 6

    if ((lista_tablero[82] == "X" and lista_tablero[65] == "X" and lista_tablero[48] == "X" and lista_tablero[31] == "X")
        or (lista_tablero[82] == "O" and lista_tablero[65] == "O" and lista_tablero[48] == "O" and lista_tablero[31] == "O")):
        return True

    if ((lista_tablero[84] == "X" and lista_tablero[67] == "X" and lista_tablero[50] == "X" and lista_tablero[33] == "X")
        or (lista_tablero[84] == "O" and lista_tablero[67] == "O" and lista_tablero[50] == "O" and lista_tablero[33] == "O")):
        return True

    if ((lista_tablero[86] == "X" and lista_tablero[69] == "X" and lista_tablero[52] == "X" and lista_tablero[35] == "X")
        or (lista_tablero[86] == "O" and lista_tablero[69] == "O" and lista_tablero[52] == "O" and lista_tablero[35] == "O")):
        return True

    if ((lista_tablero[88] == "X" and lista_tablero[71] == "X" and lista_tablero[54] == "X" and lista_tablero[37] == "X")
        or (lista_tablero[88] == "O" and lista_tablero[71] == "O" and lista_tablero[54] == "O" and lista_tablero[37] == "O")):
        return True

    #Fila 5

    if ((lista_tablero[67] == "X" and lista_tablero[50] == "X" and lista_tablero[33] == "X" and lista_tablero[16] == "X")
        or (lista_tablero[67] == "O" and lista_tablero[50] == "O" and lista_tablero[33] == "O" and lista_tablero[16] == "O")):
        return True

    if ((lista_tablero[69] == "X" and lista_tablero[52] == "X" and lista_tablero[35] == "X" and lista_tablero[18] == "X")
        or (lista_tablero[69] == "O" and lista_tablero[52] == "O" and lista_tablero[35] == "O" and lista_tablero[18] == "O")):
        return True

    if ((lista_tablero[71] == "X" and lista_tablero[54] == "X" and lista_tablero[37] == "X" and lista_tablero[20] == "X")
        or (lista_tablero[71] == "O" and lista_tablero[54] == "O" and lista_tablero[37] == "O" and lista_tablero[20] == "O")):
        return True

    if ((lista_tablero[73] == "X" and lista_tablero[56] == "X" and lista_tablero[39] == "X" and lista_tablero[22] == "X")
        or (lista_tablero[73] == "O" and lista_tablero[56] == "O" and lista_tablero[39] == "O" and lista_tablero[22] == "O")):
        return True

    #Fila 4

    if ((lista_tablero[52] == "X" and lista_tablero[35] == "X" and lista_tablero[18] == "X" and lista_tablero[1] == "X")
        or (lista_tablero[52] == "O" and lista_tablero[35] == "O" and lista_tablero[18] == "O" and lista_tablero[1] == "O")):
        return True

    if ((lista_tablero[54] == "X" and lista_tablero[37] == "X" and lista_tablero[20] == "X" and lista_tablero[3] == "X")
        or (lista_tablero[54] == "O" and lista_tablero[37] == "O" and lista_tablero[20] == "O" and lista_tablero[3] == "O")):
        return True

    if ((lista_tablero[56] == "X" and lista_tablero[39] == "X" and lista_tablero[22] == "X" and lista_tablero[5] == "X")
        or (lista_tablero[56] == "O" and lista_tablero[39] == "O" and lista_tablero[22] == "O" and lista_tablero[5] == "O")):
        return True

    if ((lista_tablero[58] == "X" and lista_tablero[41] == "X" and lista_tablero[24] == "X" and lista_tablero[7] == "X")
        or (lista_tablero[58] == "O" and lista_tablero[41] == "O" and lista_tablero[24] == "O" and lista_tablero[7] == "O")):
        return True

        #HORIZONTAL DEL 1 AL 4

    #Fila 1

    if ((lista_tablero[1] == "X" and lista_tablero[3] == "X" and lista_tablero[5] == "X" and lista_tablero[7] == "X")
        or (lista_tablero[1] == "O" and lista_tablero[3] == "O" and lista_tablero[5] == "O" and lista_tablero[7] == "O")):
        return True

    #Fila 2

    if ((lista_tablero[16] == "X" and lista_tablero[18] == "X" and lista_tablero[20] == "X" and lista_tablero[22] == "X")
        or (lista_tablero[16] == "O" and lista_tablero[18] == "O" and lista_tablero[20] == "O" and lista_tablero[22] == "O")):
        return True

    #Fila 3

    if ((lista_tablero[31] == "X" and lista_tablero[33] == "X" and lista_tablero[35] == "X" and lista_tablero[37] == "X")
        or (lista_tablero[31] == "O" and lista_tablero[33] == "O" and lista_tablero[35] == "O" and lista_tablero[37] == "O")):
        return True

    #Fila 4

    if ((lista_tablero[46] == "X" and lista_tablero[48] == "X" and lista_tablero[50] == "X" and lista_tablero[52] == "X")
        or (lista_tablero[46] == "O" and lista_tablero[48] == "O" and lista_tablero[50] == "O" and lista_tablero[52] == "O")):
        return True

    #Fila 5

    if ((lista_tablero[61] == "X" and lista_tablero[63] == "X" and lista_tablero[65] == "X" and lista_tablero[67] == "X")
        or (lista_tablero[61] == "O" and lista_tablero[63] == "O" and lista_tablero[65] == "O" and lista_tablero[67] == "O")):
        return True

    #Fila 6

    if ((lista_tablero[76] == "X" and lista_tablero[78] == "X" and lista_tablero[80] == "X" and lista_tablero[82] == "X")
        or (lista_tablero[76] == "O" and lista_tablero[78] == "O" and lista_tablero[80] == "O" and lista_tablero[82] == "O")):
        return True

    #HORIZONTAL DEL 2 AL 5

    #Fila 1

    if ((lista_tablero[3] == "X" and lista_tablero[5] == "X" and lista_tablero[7] == "X" and lista_tablero[9] == "X")
        or (lista_tablero[3] == "O" and lista_tablero[5] == "O" and lista_tablero[7] == "O" and lista_tablero[9] == "O")):
        return True

    #Fila 2

    if ((lista_tablero[18] == "X" and lista_tablero[20] == "X" and lista_tablero[22] == "X" and lista_tablero[24] == "X")
        or (lista_tablero[18] == "O" and lista_tablero[20] == "O" and lista_tablero[22] == "O" and lista_tablero[24] == "O")):
        return True

    #Fila 3

    if ((lista_tablero[33] == "X" and lista_tablero[35] == "X" and lista_tablero[37] == "X" and lista_tablero[39] == "X")
        or (lista_tablero[33] == "O" and lista_tablero[35] == "O" and lista_tablero[37] == "O" and lista_tablero[39] == "O")):
        return True

    #Fila 4

    if ((lista_tablero[48] == "X" and lista_tablero[50] == "X" and lista_tablero[52] == "X" and lista_tablero[54] == "X")
        or (lista_tablero[48] == "O" and lista_tablero[50] == "O" and lista_tablero[52] == "O" and lista_tablero[54] == "O")):
        return True

    #Fila 5

    if ((lista_tablero[63] == "X" and lista_tablero[65] == "X" and lista_tablero[67] == "X" and lista_tablero[69] == "X")
        or (lista_tablero[63] == "O" and lista_tablero[65] == "O" and lista_tablero[67] == "O" and lista_tablero[69] == "O")):
        return True

    #Fila 6

    if ((lista_tablero[78] == "X" and lista_tablero[80] == "X" and lista_tablero[82] == "X" and lista_tablero[84] == "X")
        or (lista_tablero[78] == "O" and lista_tablero[80] == "O" and lista_tablero[82] == "O" and lista_tablero[84] == "O")):
        return True

    #HORIZONTAL DEL 3 AL 6

    #Fila 1

    if ((lista_tablero[5] == "X" and lista_tablero[7] == "X" and lista_tablero[9] == "X" and lista_tablero[11] == "X")
        or (lista_tablero[5] == "O" and lista_tablero[7] == "O" and lista_tablero[9] == "O" and lista_tablero[11] == "O")):
        return True

    #Fila 2

    if ((lista_tablero[20] == "X" and lista_tablero[22] == "X" and lista_tablero[24] == "X" and lista_tablero[26] == "X")
        or (lista_tablero[20] == "O" and lista_tablero[22] == "O" and lista_tablero[24] == "O" and lista_tablero[26] == "O")):
        return True

    #Fila 3

    if ((lista_tablero[35] == "X" and lista_tablero[37] == "X" and lista_tablero[39] == "X" and lista_tablero[41] == "X")
        or (lista_tablero[35] == "O" and lista_tablero[37] == "O" and lista_tablero[39] == "O" and lista_tablero[41] == "O")):
        return True

    #Fila 4

    if ((lista_tablero[50] == "X" and lista_tablero[52] == "X" and lista_tablero[54] == "X" and lista_tablero[56] == "X")
        or (lista_tablero[50] == "O" and lista_tablero[52] == "O" and lista_tablero[54] == "O" and lista_tablero[56] == "O")):
        return True

    #Fila 5

    if ((lista_tablero[65] == "X" and lista_tablero[67] == "X" and lista_tablero[69] == "X" and lista_tablero[71] == "X")
        or (lista_tablero[65] == "O" and lista_tablero[67] == "O" and lista_tablero[69] == "O" and lista_tablero[71] == "O")):
        return True

    #Fila 6

    if ((lista_tablero[80] == "X" and lista_tablero[82] == "X" and lista_tablero[84] == "X" and lista_tablero[86] == "X")
        or (lista_tablero[80] == "O" and lista_tablero[82] == "O" and lista_tablero[84] == "O" and lista_tablero[86] == "O")):
        return True


    #HORIZONTAL DEL 4 AL 7

    #Fila 1

    if ((lista_tablero[7] == "X" and lista_tablero[9] == "X" and lista_tablero[11] == "X" and lista_tablero[13] == "X")
        or (lista_tablero[7] == "O" and lista_tablero[9] == "O" and lista_tablero[11] == "O" and lista_tablero[13] == "O")):
        return True

    #Fila 2

    if ((lista_tablero[22] == "X" and lista_tablero[24] == "X" and lista_tablero[26] == "X" and lista_tablero[28] == "X")
        or (lista_tablero[22] == "O" and lista_tablero[24] == "O" and lista_tablero[26] == "O" and lista_tablero[28] == "O")):
        return True

    #Fila 3

    if ((lista_tablero[37] == "X" and lista_tablero[39] == "X" and lista_tablero[41] == "X" and lista_tablero[43] == "X")
        or (lista_tablero[37] == "O" and lista_tablero[39] == "O" and lista_tablero[41] == "O" and lista_tablero[43] == "O")):
        return True

    #Fila 4

    if ((lista_tablero[52] == "X" and lista_tablero[54] == "X" and lista_tablero[56] == "X" and lista_tablero[58] == "X")
        or (lista_tablero[52] == "O" and lista_tablero[54] == "O" and lista_tablero[56] == "O" and lista_tablero[58] == "O")):
        return True

    #Fila 5

    if ((lista_tablero[67] == "X" and lista_tablero[69] == "X" and lista_tablero[71] == "X" and lista_tablero[73] == "X")
        or (lista_tablero[67] == "O" and lista_tablero[69] == "O" and lista_tablero[71] == "O" and lista_tablero[73] == "O")):
        return True

    #Fila 6

    if ((lista_tablero[82] == "X" and lista_tablero[84] == "X" and lista_tablero[86] == "X" and lista_tablero[88] == "X")
        or (lista_tablero[82] == "O" and lista_tablero[84] == "O" and lista_tablero[86] == "O" and lista_tablero[88] == "O")):
        return True





Menu()
    
    
    
    

    
        

   



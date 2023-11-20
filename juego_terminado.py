import random
# en este programa, se le pide al usuario que adivine un número aleatorio mediante pistas del programa. El usuario podrá elegir el nivel de dificultad del juego así como establecer un límite de intentos para adivinar el número. Si sobrepasa este número de intentos,pierde la partida.
def adivinar_numero(nivel,num_max_int):
    #
    #print(nivel)
    #limite_superior = 0
    if (int(nivel)==1):
        limite_superior = 100
    elif (int(nivel)==2):
        limite_superior= 1000
    elif (int(nivel)==3):
        limite_superior= 1000000
    elif (int(nivel)==4):
        limite_superior=1000000000000

    #print(limite_superior)
    print("¡Adivina el número!")
    numero_secreto = random.randint(0, int(limite_superior))
    contador = 0


    while True:
        intento = input("Ingresa un número entre 0 y %s : --> " % str(limite_superior))
        
        contador = contador + 1
        
        print ("Intento número: %s:" % int(contador))

        if (int(intento)<0) or (int(intento)>int(limite_superior)):
           print("NÚMERO INTRODUCIDO FUERA DE RANGO")
        else:
           if int(intento) == numero_secreto:
               print("¡Felicidades! ¡Has adivinado el número!")
               print("Ha acertado en %s intentos de %s intentos máximos posibles" % (contador, num_max_int))
               break
           elif int(intento) < numero_secreto:
               print("Has fallado. El número secreto es mayor.")
               if (int(contador) >= int(num_max_int)):
                    print("Fin del juego. Has Superado el número de intentos.")
                    break
           else:
               print("Has fallado. El número secreto es menor.")
               if (int(contador) >= int(num_max_int)):
                    print("Fin del juego. Has Superado el número de intentos.")
                    break
        print ("Tiene %s intentos más" % (int(num_max_int)-int(contador)))

dificultad = input("Ingresa un nivel de dificulatd (1=fácil, 2=intermedio, 3=avanzado y 4=experto) ")
#seleccionar nivel de dificultad, hace variar el limite superior
num_intentos_max = input("Ingresa el número de intentos máximos en que adivinar el número secreto: ")
#parametro validacion
# for i not in range(0,4):
# if i == dificutlad:
if (int(dificultad)<0) or (int(dificultad)>4):
    print("DIFICULTAD INTRODUCIDA NO PERMITIDA")
elif (int(num_intentos_max)<1):
    print("NUMERO DE INTENTOS MAXIMOS ESTABLECIDOS NO PERMITIDO")
else:
    adivinar_numero(dificultad, num_intentos_max)

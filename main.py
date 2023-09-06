import keyboard #Lee las teclas que se van presionando en el teclado

jugador_nick = input() #Solicita el nombre del jugador

print(f'¡Bienvenido, {jugador_nick}!') #Imprime mensaje de bienvenida + el nickname

''' --------------------------------------------------------------------------------- '''
continuar = True #variable para cambiar a Falso y detener el loop
while continuar: #loop infinito
    keyboard.read_key() != keyboard.KEY_UP #si la tecla que se está presionando es diferente a la flecha arriba:
    print(keyboard.read_key()) #imprime la tecla que se esté presionando mientras esta sea diferente a la flecha arriba
    if keyboard.is_pressed(keyboard.KEY_UP): #si se mantiene presionada la flecha arriba:
        continuar == False #la variable ligada al ciclo cambia a falso
        print ("Fin")
        break #y se rompe el ciclo

''' Este loop solo cumple con el ejercicio si se mantiene presionada la flecha arriba por un segundo, si solo se presiona por un milisegundo no funciona :c '''

#Eejercicio cachipun 

import random
#Definimos variables que van a sumar dsp
puntos_usuario = 0
puntos_pc = 0
rounds = 1 

#opciones que tendran los jugadores 
options = ["piedra","papel","tijera"]

print("Hola, Bienvenido al juego tradicional Chileno 'Cahipun'")

computer_option = random.choice(options)


while True:
    print("*"*10)
    print("RONDA", rounds)
    print("*"*10)

    computer_option = random.choice(options)
    user_option = input("Seleciona entre piedra, papel o tijera => ").lower()
    
    if not user_option  in options:
     print("La opción elegida no es valida, porfavor selecciona una valída")
     continue
    rounds += 1

    print("tu elegiste =>", user_option)
    print("La PC eligio =>", computer_option)
     
    if user_option == computer_option:
       (print("Empate"))    
    elif user_option == "piedra":    #OPCION PIEDRA
        if computer_option == "papel": 
            print("gana la pc")
            puntos_pc += 1
        else:
            computer_option == "tijera"
            print("ganas tú")
            puntos_usuario += 1 
    elif user_option == "tijera":   #OPCION TIJERA 
        if computer_option == "piedra":
            print("gana la pc")
            puntos_pc += 1
        else:
            computer_option == "papel"
            print("ganas tú")
            puntos_usuario += 1 
    elif user_option == "papel":   #OPCION PAPEL 
        if computer_option == "tijera":
            print("gana la pc")
            puntos_pc += 1
        else:
            computer_option == "piedra"
            print("ganas tú")
            puntos_usuario += 1 
    
    if puntos_usuario == 3 :
        print("El usuario gano a la maquiná")
        break   
    if puntos_pc == 3 :
        print("El PC ganó")
        break

    print("-"*5)
    print("LA PUNTUACION ES:"
        "Usuario",puntos_usuario,
        "PC",puntos_pc)
    print("-"*5)
    

    
  

        


          
   
   
    


            


    
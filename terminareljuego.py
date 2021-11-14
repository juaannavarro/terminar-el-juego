def adivina_numero(num_max):
    import random 
    numero=random.randint(0,num_max)

    numero_intento=0
    
    encontrado = False
    while not encontrado:

        print("elige un numero del 0 al ",num_max,":")
        intento=int(input())
        
        if intento<numero:
            print("demasiado pequeño")
        if intento>numero:
            print("demasiado grande")
        if intento==numero:
            print("acertaste")
            encontrado = True

        numero_intento=numero_intento+1
    print("numero de intentos", numero_intento)


def elegirOpcion():
    opcion_valida=False
    num=0
   
    while(not opcion_valida):
        
        num=int(input("Elige entre 1 y 5: "))
        if(num>=1 and num<=5):
            opcion_valida=True
        else:
            print("El valor no esta entre el 1 y el 5")
            
    return num

def ayuda(nivel):
    if nivel==1:
        print("0-100")
    elif nivel==2:
        print("0-1000")
    elif nivel==3:
        print("0-1000000")
    elif nivel==4:
        print("0-1000000000")
    


salir=False
opcion=0

while not salir:
    print("Menu")
    print("1-Nivel simple")
    print("2-Nivel intermedio")
    print("3-Nivel avanzado")
    print("4-Nivel experto")
    print("5-Salir")

    print("Elige una opcion")

    opcion = elegirOpcion()

    print("Opcion elegida ", opcion)

    if opcion!=5:
        aceptar_ayuda=input("¿quiere ayuda?s/n: ")
        if aceptar_ayuda=="s" or aceptar_ayuda=="S":
            ayuda(opcion)
    
    
    if opcion==1:
        print("nivel simple")
        adivina_numero(100)
    elif opcion==2:
        print("nivel intermedio")
        adivina_numero(1000)
    elif opcion==3:
        print("nivel avanzado")
        adivina_numero(1000000)
    elif opcion==4:
        print("nivel experto")
        adivina_numero(1000000000)
    elif opcion==5:
        salir=True
        print("fin del programa")

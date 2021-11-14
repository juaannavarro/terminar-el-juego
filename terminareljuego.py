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

    aceptar_ayuda=input("¿quiere ayuda?s/n: ")
    if (aceptar_ayuda=="s" or aceptar_ayuda=="S") and opcion>=1 and opcion<=4:
        ayuda(opcion)
    




    if opcion==1:
        print("nivel simple")
    elif opcion==2:
        print("nivel intermedio")
    elif opcion==3:
        print("nivel avanzado")
    elif opcion==4:
        print("nivel experto")
    elif opcion==5:
        salir=True
        print("fin del programa")
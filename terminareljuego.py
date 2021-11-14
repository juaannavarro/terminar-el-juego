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

    if opcion==1:
        print("primera funcion")
    elif opcion==2:
        print("segunda funcion")
    elif opcion==3:
        print("tercera funcion")
    elif opcion==4:
        print("cuarta funcion")
    elif opcion==5:
        salir=True
        print("fin del programa")
def elegir_opcion():
    opcion_valida=False
    num=0
    while(not opcion_valida):
        
        num=int(input("Elige entre 1 y 5"))
        if(num>=1 or num<=5):
            opcion_valida=True
        else:
            print("el valor no esta entre el 1 y el 5")
    return num

print("Menu")
print("1-Nivel simple")
print("2-Nivel intermedio")
print("3-Nivel avanzado")
print("4-Nivel experto")
print("5-Salir")

print("Elige una opcion")
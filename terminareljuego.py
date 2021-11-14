import random 

numero=random.randint(0,99)
print("Introduzca el numero a adivinar", numero)
while True:
    numero=input("Introduzca un numero entre 0 y 99 incluidos")
    try:
        numero=int(numero)
    except:
        pass
    else:
        if 0<= numero <= 99:
            break
print("Intenta adivinar el numero")
while True:
    while True:
        intento=input("Introduce un numero entre 0 y 99 incluidos")
        try:
            intento=int(intento)
        except:
            pass
        else:
            if 0<= intento <=99:
                break
if intento< (numero):
    print("demasiado pequeño")
if intento> (numero):
    print("demasiado grande")
if intento== (numero):
    print("Has acertado")
            
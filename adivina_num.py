NUMERO_SECRETO = 67

while True:
    n = int(input("Introduce un numero entero: "))
    if n < 0:
        print("El numero debe ser mayor que 0")
    elif n < NUMERO_SECRETO:
        print("El numero secreto es mayor.")
    elif n > NUMERO_SECRETO:
        print("El numero secreto es menor.")
    else:
        print("HAS ACERTADO BB :)")
        break

suma = 0

for i in range (1, 6):
    n = int(input("Introduce un numero entero: "))

    if n > 0:
        suma += n
    else:
        continue #else y continue no son necesarios, pero los dejo para que se vea la estructura del if-else

print(f"suma de los numeros positivos: {suma}")  
#CONSTANTES
TEMPERATURA_MAXIMA = 100.0
TEMPERATURA_MINIMA = 0.0

#VARIABLES
temperatura = 0.0

#contadores y acumuladores
alertas_rojas = 0
suma_temperaturas = 0.0
temp_anterior = None

#bandera
emergencia = False

#validacion con while
num_lecturas = int(input("Cuantas lecturas de temperatura quiere registrar: "))
while num_lecturas <=0:
    print("Error, debe ser un numero positivo")
    num_lecturas = int(input("Cuantas lecturas de temperatura quiere registrar: "))

print(f"numero de lecturas: {num_lecturas}")


for i in range (1, num_lecturas + 1):

    while True: #Repetir la lectura si esta mal ingresada
         try:
            temp = float(input("Introduce la temperatura: "))
            if temp < -273.15:
                raise ValueError("La temperatura no puede ser menor que el cero absoluto.")
            break
         except ValueError as e:
            print(f"Error: {e}")
    
    suma_temperaturas += temp

    if temp > TEMPERATURA_MAXIMA:
        print("Peligro, la temperatura supera la maxima!!!")
        alertas_rojas += 1

        if temp_anterior is not None and temp_anterior > TEMPERATURA_MAXIMA:
            print("DOS TEMP CRITICAS!!!")
            emergencia = True

    elif temp < TEMPERATURA_MINIMA:
        print("Alerta de congelación!!!")

        if temp_anterior is not None and temp_anterior < TEMPERATURA_MINIMA:
            print("DOS TEMP CRITICAS!!!")
            emergencia = True
    else: 
        print("Temperatura normal")

    temp_anterior = temp

#Resultados finales
print(f"Numero de alertas rojas: {alertas_rojas}")
print(f"Suma de temperaturas: {suma_temperaturas}")
print(f"Promedio de temperaturas: {suma_temperaturas / num_lecturas if num_lecturas > 0 else 0}")
if emergencia:
    print("EMERGENCIA: Se detectaron dos o más condiciones críticas.")

try:
    dividendo = float(input("Introduce el primer numero: "))
    divisor = float(input("Introduce el segundo numero: "))
    resultado = dividendo / divisor
    print(f"Resultado: {resultado}")

except ValueError:
    print("Error: debes introducir valores numericos")
except ZeroDivisionError:
    print("Error: no se puede dividir entre 0")




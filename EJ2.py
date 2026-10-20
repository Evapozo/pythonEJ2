# Proyecto: Taquilla de cine 
# Autores: Eva Pozo y Marcos Fernandez

#Inicialización de variables para llevar un registro de las operaciones realizadas, el número total de entradas vendidas y el total recaudado.
total_operaciones = 0 
total_entradas = 0 
total_recaudado = 0.0 

#Menú principal del programa, donde el usuario puede elegir entre vender entradas, consultar el resumen de ventas o salir del programa.
while True: 
    print("\n========== TAQUILLA DE CINE ==========") 
    print("1. Vender entradas") 
    print("2. Consultar resumen de ventas") 
    print("3. Salir") 
 
    opcion = input("Selecciona una opción: ") 

    #OPCIÓN 1: Vender entradas
    if opcion == "1": 
        #Solicitar los datos del cliente y calcular el precio de la entrada según la edad
        nombre_cliente = input("Ingrese el nombre del cliente: ")

        #En la edad utilizamos try-except para controlar que el usuario ingrese un número entero y no un valor negativo 
        #tanto en la edad como en el número de entradas a comprar.
        try:
            edad_cliente = int(input("Edad del cliente: "))
            if edad_cliente < 0:
                print("Error: la edad no puede ser negativa.")
                continue
                
            num_entradas = int(input("Número de entradas: "))
            if num_entradas <= 0:
                print("Error: el número de entradas debe ser mayor que cero.")
                continue
            
        except ValueError:
            print("Error: debes introducir un número entero.")
            continue
        #Estructura de seleción para determinar el precio de la entrada según la edad del cliente
        #guardamos el tipo de entrada y el precio en variables para luego poder mostrarlo al usuario y calcular el total a pagar.
        if edad_cliente < 5:
            tipo_entrada = "Infantil gratuita"
            precio_entrada = 0.0
        elif edad_cliente >= 5 and edad_cliente <= 17:
            tipo_entrada = "Menores"
            precio_entrada = 5.0
        elif edad_cliente >= 18 and edad_cliente <= 64:
            tipo_entrada = "General"
            precio_entrada = 9.0
        else:
            tipo_entrada = "Sénior"
            precio_entrada = 6.0

        #Calculo del total a pagar por el cliente
        total_compra = num_entradas * precio_entrada
 
    elif opcion == "2": 
        # Mostrar el resumen de ventas 
        pass 
 
    elif opcion == "3": 

        # Finalizar el programa 
        break 
    else: 
        print("Opción no válida") 
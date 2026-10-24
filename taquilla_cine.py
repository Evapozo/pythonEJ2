# Proyecto: Taquilla de cine
# Autores: Eva Pozo y Marcos Fernández


# Variables globales
total_operaciones = 0      # Contador: número de ventas realizadas
total_entradas = 0         # Acumulador: entradas vendidas en total
total_recaudado = 0.0      # Acumulador: dinero recaudado en total

# Ampliación: contador de entradas vendidas de cada tipo
entradas_infantiles = 0
entradas_menores = 0
entradas_generales = 0
entradas_senior = 0

# Constantes globales (evitan números mágicos en el código)
PRECIO_INFANTIL = 0.0
PRECIO_MENORES = 5.0
PRECIO_GENERAL = 9.0
PRECIO_SENIOR = 6.0
MAXIMO_ENTRADAS = 10           # Ampliación: límite por operación
ENTRADAS_PARA_DESCUENTO = 5    # Ampliación: mínimo para tener descuento
PORCENTAJE_DESCUENTO = 0.10    # Ampliación: 10 %

#Menú principal del programa, donde el usuario puede elegir entre vender entradas, consultar el resumen de ventas o salir del programa.
while True:
    print("\n========== TAQUILLA DE CINE ==========")
    print("1. Vender entradas")
    print("2. Consultar resumen de ventas")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        # OPCIÓN 1: VENDER ENTRADAS

        # Datos del cliente
        nombre_cliente = input("Nombre del cliente: ").strip()
        if nombre_cliente == "":
            print("Error: el nombre no puede estar vacío.")
            continue  # Vuelve al menú

        # Control de excepciones: si el texto no es un entero int() lanza ValueError
        try:
            edad = int(input("Edad del cliente: "))
            numero_entradas = int(input("Número de entradas: "))
        except ValueError:
            print("Error: debes introducir un número entero.")
            continue  # Vuelve al menú sin registrar la venta

        # Validación de los rangos permitidos
        if edad < 0:
            print("Error: la edad no puede ser negativa.")
            continue
        if numero_entradas <= 0:
            print("Error: el número de entradas debe ser mayor que cero.")
            continue
        if numero_entradas > MAXIMO_ENTRADAS:
            print(f"Error: no se pueden vender más de {MAXIMO_ENTRADAS} entradas por operación.")
            continue

        # Selección del tipo de entrada y del precio según la edad
        if edad < 5:
            tipo_entrada = "Infantil gratuita"
            precio_entrada = PRECIO_INFANTIL
        elif edad >= 5 and edad <= 17:
            tipo_entrada = "Menores"
            precio_entrada = PRECIO_MENORES
        elif edad >= 18 and edad <= 64:
            tipo_entrada = "General"
            precio_entrada = PRECIO_GENERAL
        else:
            tipo_entrada = "Sénior"
            precio_entrada = PRECIO_SENIOR

        # Cálculo del total de la compra
        total_compra = precio_entrada * numero_entradas

        # Ampliación: descuento del 10 % a partir de 5 entradas
        descuento = 0.0
        if numero_entradas >= ENTRADAS_PARA_DESCUENTO:
            descuento = total_compra * PORCENTAJE_DESCUENTO
            total_compra = total_compra - descuento

        # Mostrar el ticket
        print("\n========== TICKET ==========")
        print(f"Cliente: {nombre_cliente}")
        print(f"Tipo: {tipo_entrada}")
        print(f"Precio por entrada: {precio_entrada:.2f} €")
        print(f"Número de entradas: {numero_entradas}")
        if descuento > 0:
            print(f"Descuento (10 %): -{descuento:.2f} €")
        print(f"TOTAL: {total_compra:.2f} €")
        print("============================")

        # Actualizar contadores y acumuladores
        total_operaciones += 1                # contador
        total_entradas += numero_entradas     # acumulador
        total_recaudado += total_compra       # acumulador

        # Ampliación: contar entradas por tipo
        if tipo_entrada == "Infantil gratuita":
            entradas_infantiles += numero_entradas
        elif tipo_entrada == "Menores":
            entradas_menores += numero_entradas
        elif tipo_entrada == "General":
            entradas_generales += numero_entradas
        else:
            entradas_senior += numero_entradas

    elif opcion == "2":
        #OPCIÓN 2: RESUMEN DE VENTAS
        print("\n========== RESUMEN DE VENTAS ==========")
        print(f"Operaciones realizadas: {total_operaciones}")
        print(f"Entradas vendidas: {total_entradas}")
        print(f"Recaudación total: {total_recaudado:.2f} €")

        # Ampliación: recaudación media (evitando dividir entre cero)
        if total_operaciones > 0:
            recaudacion_media = total_recaudado / total_operaciones
        else:
            recaudacion_media = 0.0
        print(f"Recaudación media por operación: {recaudacion_media:.2f} €")

        # Ampliación: desglose por tipo de entrada
        print("--- Entradas por tipo ---")
        print(f"Infantil gratuita: {entradas_infantiles}")
        print(f"Menores: {entradas_menores}")
        print(f"General: {entradas_generales}")
        print(f"Sénior: {entradas_senior}")
        print("=======================================")

    elif opcion == "3":
        # OPCIÓN 3: SALIR
        print("Programa finalizado.")
        print("Gracias por utilizar la taquilla.")
        break  # Termina el bucle while y el programa

    else:
        # OPCIÓN NO VÁLIDA
        print("Opción no válida. Selecciona una opción del 1 al 3.")

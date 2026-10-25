# Proyecto: Taquilla de cine
# Autores: Eva Pozo y Marcos Fernández
#
# Estructuras utilizadas:
#   - Repetición:  while True (mantiene activo el menú)
#   - Selección:   if / elif / else (menú, tipo de entrada, descuentos)
#   - Salto:       break (salir) y continue (volver al menú ante un error)
#   - Excepciones: try-except ValueError y raise ValueError

# VARIABLES GLOBALES: contadores y acumuladores del resumen

total_operaciones = 0      # Contador: número de ventas realizadas (suma 1 por venta)
total_entradas = 0         # Acumulador: entradas vendidas en total
total_recaudado = 0.0      # Acumulador: dinero recaudado en total

# AMPLIACIÓN: contabilizar las entradas vendidas de cada tipo.
# Un contador por tipo; se muestran en el resumen de ventas (opción 2).
entradas_infantiles = 0
entradas_menores = 0
entradas_generales = 0
entradas_senior = 0

# CONSTANTES: evitan "números mágicos" en el código
# y permiten cambiar un precio o un límite en un único sitio.
PRECIO_INFANTIL = 0.0          # Menores de 5 años
PRECIO_MENORES = 5.0           # De 5 a 17 años
PRECIO_GENERAL = 9.0           # De 18 a 64 años
PRECIO_SENIOR = 6.0            # 65 años o más
MAXIMO_ENTRADAS = 10           # AMPLIACIÓN: máximo de entradas por operación
ENTRADAS_PARA_DESCUENTO = 5    # AMPLIACIÓN: entradas mínimas para el descuento de grupo
PORCENTAJE_DESCUENTO = 0.10    # AMPLIACIÓN: descuento de grupo del 10 %
PORCENTAJE_ESTUDIANTE = 0.20   # AMPLIACIÓN: descuento del 20 % con carnet de estudiante


# FUNCIONES AUXILIARES
def validar_datos(edad, numero_entradas):
    """Comprueba que la edad y el número de entradas tengan un valor válido.

    Estos datos ya son números enteros (int() no ha fallado), pero su VALOR
    puede ser incorrecto. Si lo es, lanza un ValueError con raise para que
    lo capture el try-except del programa principal.
    """
    if edad < 0:
        raise ValueError("la edad no puede ser negativa.") # raise lanza un ValueError cuando el dato es un entero pero
    # su valor no es válido (edad negativa, entradas <= 0 o más de 10).
    if numero_entradas <= 0:
        raise ValueError("el número de entradas debe ser mayor que cero.")
    # AMPLIACIÓN: impedir la venta de más de diez entradas en una operación
    if numero_entradas > MAXIMO_ENTRADAS:
        raise ValueError(f"no se pueden vender más de {MAXIMO_ENTRADAS} entradas por operación.")


def pedir_si_no(mensaje):
    """Hace una pregunta de sí o no. Devuelve True solo si el usuario responde 's'.

    strip() quita los espacios sobrantes y lower() pasa a minúsculas,
    de modo que " S ", "s" y "S" se interpretan igual.
    """
    respuesta = input(mensaje + " (s/n): ").strip().lower()
    return respuesta == "s"


# MENÚ PRINCIPAL
# El bucle while True mantiene el programa activo: el menú vuelve a
# mostrarse después de cada operación hasta que se elige la opción 3.
while True:
    print("\n========== TAQUILLA DE CINE ==========")
    print("1. Vender entradas")
    print("2. Consultar resumen de ventas")
    print("3. Salir")
    print("4. Reiniciar estadísticas") # AMPLIACIÓN

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        # OPCIÓN 1: VENDER ENTRADAS
    
        # NOMBRE DEL CLIENTE
        # strip() elimina los espacios del principio y del final.
        nombre_cliente = input("Nombre del cliente: ").strip()

        # El nombre se valida justo al leerlo: si está vacío no tiene sentido
        # pedir el resto de datos, así que se avisa y se vuelve al menú.
        if nombre_cliente == "":
            print("Error: el nombre no puede estar vacío.")
            continue  # Vuelve al menú sin pedir más datos

        # EDAD Y NÚMERO DE ENTRADAS
        # input() devuelve texto; int() lo convierte a entero. Si el usuario
        # escribe "veinte", "3.5" o nada, int() lanza un ValueError.
        try:
            edad = int(input("Edad del cliente: "))
            numero_entradas = int(input("Número de entradas: "))
        except ValueError:
            print("Error: debes introducir un número entero.")
            continue  # Vuelve al menú sin registrar la venta

        # VALIDACIÓN DE DATOS
        # validar_datos() usa raise ValueError si la edad es negativa o el
        # número de entradas no es válido. Se captura aquí para mostrar el
        # mensaje y volver al menú.
        try:
            validar_datos(edad, numero_entradas)
        except ValueError as error:
            print(f"Error: {error}")
            continue  # Vuelve al menú sin registrar la venta

        # TIPO DE ENTRADA Y PRECIO
        # Estructura de selección if-elif-else. Los tramos intermedios usan
        # condiciones compuestas con "and": la edad debe cumplir las dos
        # comparaciones a la vez (por ejemplo, ser >= 5 Y ser <= 17).
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

        # AMPLIACIÓN: preguntar si el cliente dispone de carnet de estudiante.
        # tiene_carnet vale True si responde "s" y False en cualquier otro caso.
        tiene_carnet = pedir_si_no("¿El cliente dispone de carnet de estudiante?")

        # CÁLCULO DEL TOTAL DE LA COMPRA
        # Total bruto = precio por entrada x número de entradas.
        # round(..., 2) redondea a céntimos para evitar errores de decimales.
        total_bruto = round(precio_entrada * numero_entradas, 2)

        # AMPLIACIÓN: se hace un descuento del 20 % por carnet de estudiante.
        # Condición compuesta con "and": solo se aplica si tiene carnet Y la
        # entrada no es gratuita (no tiene sentido descontar sobre 0 €).
        descuento_carnet = 0.0
        if tiene_carnet and precio_entrada > 0:
            descuento_carnet = round(total_bruto * PORCENTAJE_ESTUDIANTE, 2)
        total_compra = round(total_bruto - descuento_carnet, 2)

        # AMPLIACIÓN: descuento de grupo del 10 % a partir de 5 entradas.
        # Se calcula sobre el total que queda después del descuento de carnet.
        descuento_grupo = 0.0
        if numero_entradas >= ENTRADAS_PARA_DESCUENTO:
            descuento_grupo = round(total_compra * PORCENTAJE_DESCUENTO, 2)
            total_compra = round(total_compra - descuento_grupo, 2)

        # MOSTRAR TICKET DE VENTA
        # Los importes se muestran con dos decimales (:.2f).
        # Las líneas de descuento solo aparecen si realmente hubo descuento.
        print("\n========== TICKET ==========")
        print(f"Cliente: {nombre_cliente}")
        print(f"Tipo: {tipo_entrada}")
        print(f"Precio por entrada: {precio_entrada:.2f} €")
        print(f"Número de entradas: {numero_entradas}")
        if descuento_carnet > 0:
            print(f"Descuento carnet estudiante (20 %): -{descuento_carnet:.2f} €")
        if descuento_grupo > 0:
            print(f"Descuento (10 %): -{descuento_grupo:.2f} €")
        print(f"TOTAL: {total_compra:.2f} €")
        print("============================")

        # AMPLIACIÓN: permitir cancelar la compra antes de confirmarla.
        # Si el usuario no confirma, continue vuelve al menú ANTES de llegar a
        # las líneas que actualizan los acumuladores, así que no se registra nada.
        if not pedir_si_no("¿Confirmar la compra?"):
            print("Compra cancelada. No se ha registrado la venta.")
            continue  # Vuelve al menú sin registrar nada

        # ACTUALIZAR CONTADORES Y ACUMULADORES
        # Solo se llega aquí si todos los datos son válidos y la compra se ha
        # confirmado; por eso el resumen nunca incluye ventas erróneas.
        total_operaciones += 1                                       # contador: +1 por venta
        total_entradas += numero_entradas                            # acumulador: suma las entradas
        total_recaudado = round(total_recaudado + total_compra, 2)   # acumulador: suma el dinero

        # AMPLIACIÓN: sumar las entradas al contador de su tipo.
        if tipo_entrada == "Infantil gratuita":
            entradas_infantiles += numero_entradas
        elif tipo_entrada == "Menores":
            entradas_menores += numero_entradas
        elif tipo_entrada == "General":
            entradas_generales += numero_entradas
        else:
            entradas_senior += numero_entradas

        print("Venta registrada correctamente.")

    elif opcion == "2":
        # OPCIÓN 2: RESUMEN DE VENTAS
    
        print("\n========== RESUMEN DE VENTAS ==========")
        print(f"Operaciones realizadas: {total_operaciones}")
        print(f"Entradas vendidas: {total_entradas}")
        print(f"Recaudación total: {total_recaudado:.2f} €")

        # AMPLIACIÓN: recaudación media por operación.
        # Se comprueba que haya operaciones para evitar dividir entre cero.
        if total_operaciones > 0:
            recaudacion_media = round(total_recaudado / total_operaciones, 2)
        else:
            recaudacion_media = 0.0
        print(f"Recaudación media por operación: {recaudacion_media:.2f} €")

        # AMPLIACIÓN: desglose de entradas vendidas por tipo.
        print("--- Entradas por tipo ---")
        print(f"Infantil gratuita: {entradas_infantiles}")
        print(f"Menores: {entradas_menores}")
        print(f"General: {entradas_generales}")
        print(f"Sénior: {entradas_senior}")
        print("=======================================")

    elif opcion == "3":
        # OPCIÓN 3: SALIR
        # break termina el bucle while y el programa.
        print("Programa finalizado.")
        print("Gracias por utilizar la taquilla.")
        break

    elif opcion == "4":
        # OPCIÓN 4: REINICIAR ESTADÍSTICAS
        # AMPLIACIÓN: pone a cero todos los contadores y acumuladores,
        # pero antes pide confirmación para evitar borrar los datos sin querer.
        if pedir_si_no("¿Seguro que quieres reiniciar todas las estadísticas?"):
            total_operaciones = 0
            total_entradas = 0
            total_recaudado = 0.0
            entradas_infantiles = 0
            entradas_menores = 0
            entradas_generales = 0
            entradas_senior = 0
            print("Estadísticas reiniciadas.")
        else:
            print("Reinicio cancelado.")

    else:
        # OPCIÓN NO VÁLIDA: aviso y el menú vuelve a mostrarse.
        print("Opción no válida. Selecciona una opción del 1 al 4.")

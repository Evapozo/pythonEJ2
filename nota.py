nota = float(input("Ingrese la nota: "));

#if nota < 5:
#    print("Suspenso")
#elif nota >= 5 and nota <= 6.99:
#    print("Aprobado")
#elif nota >= 7 and nota <= 8.99:
#    print("Notable")
#elif nota >= 9 and nota <= 10:
#    print("Sobresaliente")
#else:
#    print("error introduce una nota valida")

if nota <0 or nota > 10:
    print("error")
elif nota < 5:
    print("Suspenso")
elif nota <= 6.99:
    print("Aprobado")
elif nota <= 8.99:
    print("Notable")
else:
    print("Sobresaliente")
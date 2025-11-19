import datetime

print("=== 1. FECHA Y HORA ACTUAL ===")
ahora = datetime.datetime.now()
print("Fecha y hora actual:", ahora)


print("\n=== 2. CÁLCULO DE EDAD ===")
while True:
    try:
        nacimiento = int(input("Introduce tu año de nacimiento: "))
        año_actual = datetime.date.today().year

        if nacimiento > año_actual:
            print("Ese año es mayor que el actual. De momento regreso al futuro es una peli.\n")
        else:
            edad = año_actual - nacimiento
            print("Tu edad es:", edad)
            break
    except ValueError:
        print("Introduce un número entero.\n")


print("\n=== 3. DÍAS RESTANTES DEL AÑO ===")
hoy = datetime.date.today()
fin_de_año = hoy.replace(month=12, day=31)
dias_restantes = (fin_de_año - hoy).days
print("Días restantes para que termine el año:", dias_restantes)

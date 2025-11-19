import math

def pedir_numero(mensaje):

    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Error: Debes introducir un número válido.\n")

# 1. Cálculo de raíz cuadrada (solo números >= 0)
while True:
    numero = pedir_numero("Introduce un número para calcular su raíz cuadrada: ")
    if numero < 0:
        print("Error: No se puede calcular la raíz cuadrada de un número negativo en el conjunto de los números reales.\n")
    else:
        break

raiz = math.sqrt(numero)
print(f"La raíz cuadrada de {numero} es: {raiz}")

# 2. Área de un círculo (radio > 0)
while True:
    radio = pedir_numero("\nIntroduce el radio de un círculo: ")
    if radio <= 0:
        print("Error: El radio debe ser mayor que 0.\n")
    else:
        break

area = math.pi * math.pow(radio, 2)
print(f"El área del círculo con radio {radio} es: {area}")

# 3. Seno y coseno de un ángulo
angulo = pedir_numero("\nIntroduce un ángulo en grados: ")
radianes = math.radians(angulo)
seno = math.sin(radianes)
coseno = math.cos(radianes)

print(f"El seno de {angulo} grados es: {seno}")
print(f"El coseno de {angulo} grados es: {coseno}")

import random

# 1. Juego de adivinar el número
print("Juego: Adivina el número")
numero_secreto = random.randint(1, 10)
intento = int(input("Adivina el número (entre 1 y 10): "))

if intento == numero_secreto:
    print("¡Correcto! Has adivinado el número.")
else:
    print(f"Incorrecto. El número era {numero_secreto}.")
print("-" * 40)

# 2. Promedio de tres números aleatorios
print(" Promedio de números aleatorios")
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
num3 = random.randint(1, 100)

print("Números generados:", num1, num2, num3)

promedio = (num1 + num2 + num3) / 3
print("Promedio:", promedio)
print("-" * 40)

# 3. Simulación de un dado
print("Simulación de un dado")
dado = random.randint(1, 6)
print("El dado muestra:", dado)

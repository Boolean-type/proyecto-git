import time

# 1. Temporizador simple
print("Temporizador")
for numero in [3, 2, 1]:
    print(f"{numero}...")
    time.sleep(1)  # pausa de 1 segundo
print("¡Listo!")
print("-" * 40)

# 2. Medir tiempo de escritura
print("Medir tiempo de escritura")
print("Escribe tu nombre y presiona Enter:")

inicio = time.time()
nombre = input()
fin = time.time()

tiempo_total = fin - inicio

print(f"Has tardado {tiempo_total:.2f} segundos en escribir tu nombre: {nombre}")

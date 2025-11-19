import os

# 1. Mostrar el directorio de trabajo actual
print("Directorio actual:")
print(os.getcwd())
print("-" * 40)

# 2. Crear una nueva carpeta llamada "prueba_python"
nombre_carpeta = "prueba_python"


if not os.path.exists(nombre_carpeta):
    os.mkdir(nombre_carpeta)
    print(f"Carpeta '{nombre_carpeta}' creada correctamente.")
else:
    print(f"La carpeta '{nombre_carpeta}' ya existe.")
print("-" * 40)

# 3. Listar archivos y carpetas en el directorio actual
print("Contenido del directorio actual:")
for elemento in os.listdir():
    print("-", elemento)

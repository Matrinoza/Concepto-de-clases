# Leer nombre y apellido
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

# Crear conjunto de letras prohibidas (mayúsculas y minúsculas)
prohibidas = set(nombre + apellido)

# Leer contraseña
contraseña = input("Ingrese su contraseña: ")

# Verificar si hay letras prohibidas en la contraseña
letras_invalidas = set(contraseña).intersection(prohibidas)

if letras_invalidas:
    print("❌ Contraseña no válida.")
    print("Contiene letras no permitidas:", ', '.join(letras_invalidas))
else:
    print("✅ Contraseña válida. No contiene letras de tu nombre ni apellido.")

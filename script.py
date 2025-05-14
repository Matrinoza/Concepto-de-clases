import random

#Clase S de abecedario

abecedario_Minuscula = "abcdefghijklmnñopqrstuvwxyz"
abecedario_Mayuscula = abecedario_Minuscula.upper()
S = set(abecedario_Minuscula + abecedario_Mayuscula)

# Entrada del usuario
Nombre = input("Nombre: ")
Apellido = input("Apellido: ")

#Clases A y B
A = set(Nombre)
B = set(Apellido)

#Union A y B
union_AB = A.union(B)

#Diferencia
C = S.difference(union_AB)

#Verificacion de letras disponibles
if len(C) < 8:
    print("No se puede generar una contraseña")
else:
    palabra_generada = ''.join(random.sample(list(C), k=8))
    print("Contraseña generada:", palabra_generada)
import random

class ConjuntoLetras:
    def __init__(self, contenido):
        self.letras = set(contenido)

    def union(self, otro):
        return ConjuntoLetras(self.letras.union(otro.letras))

    def diferencia(self, otro):
        return ConjuntoLetras(self.letras.difference(otro.letras))

    def contiene(self, letra):
        return letra in self.letras

    def como_lista(self):
        return list(self.letras)


class S(ConjuntoLetras):
    def __init__(self):
        abecedario_minusculas = "abcdefghijklmnñopqrstuvwxyz"
        abecedario_mayusculas = abecedario_minusculas.upper()
        super().__init__(abecedario_minusculas + abecedario_mayusculas)


# Entrada de datos
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

# Crear conjuntos
conjunto_s = S()
conjunto_a = ConjuntoLetras(nombre)
conjunto_b = ConjuntoLetras(apellido)
union_ab = conjunto_a.union(conjunto_b)
conjunto_c = conjunto_s.diferencia(union_ab)

# Verificar que C tenga al menos 8 letras
if len(conjunto_c.letras) < 8:
    print("❌ No se puede generar una contraseña: muy pocas letras disponibles.")
else:
    # Generar contraseña de 8 caracteres
    contraseña_generada = ''.join(random.sample(conjunto_c.como_lista(), k=8))
    print("✅ Contraseña generada:", contraseña_generada)

    # Verificar que no tenga letras del nombre o apellido
    letras_invalidas = set(contraseña_generada).intersection(union_ab.letras)
    if letras_invalidas:
        print("⚠️ Advertencia: la contraseña contiene letras del nombre o apellido:", ', '.join(letras_invalidas))
    else:
        print("✅ La contraseña cumple correctamente con los criterios.")

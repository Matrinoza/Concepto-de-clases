class ConjuntoLetras:
    def __init__(self, contenido):
        self.letras = set(contenido)

    def union(self, otro):
        return ConjuntoLetras(self.letras.union(otro.letras))

    def diferencia(self, otro):
        return ConjuntoLetras(self.letras.difference(otro.letras))

    def interseccion(self, otro):
        return self.letras.intersection(otro.letras)

    def como_lista(self):
        return list(self.letras)


class S(ConjuntoLetras):
    def __init__(self):
        abecedario_minusculas = "abcdefghijklmnñopqrstuvwxyz"
        abecedario_mayusculas = abecedario_minusculas.upper()
        super().__init__(abecedario_minusculas + abecedario_mayusculas)


# Usuario
nombre = input("Nombre: ")
apellido = input("Apellido: ")

# Conjuntos
conjunto_s = S()
conjunto_a = ConjuntoLetras(nombre)
conjunto_b = ConjuntoLetras(apellido)
union_ab = conjunto_a.union(conjunto_b)
conjunto_c = conjunto_s.diferencia(union_ab)

print("\nLetras prohibidas (A ∪ B):", sorted(union_ab.letras))
print("Letras permitidas (C = S - (A ∪ B)):", sorted(conjunto_c.letras))

# Como elegir contraseña
contraseña = input("\nIngrese la contraseña que desea utilizar: ")

# Verificacion
conjunto_contraseña = ConjuntoLetras(contraseña)
letras_invalidas = conjunto_contraseña.interseccion(union_ab)

if letras_invalidas:
    print("❌ Contraseña no válida.")
    print("Contiene las letras :", ', '.join(letras_invalidas))
else:
    print("✅ Contraseña válida.")

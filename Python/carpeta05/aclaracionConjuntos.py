conjunto = {"manzana", "enero", "c", "D"}
conjunto2 = {"manzana", "2", "Rojo", "uno"}
conjunto3 = {"manzana", "uno"}

'''
print(type(conjunto))

conjunto2 = set()
print(type(conjunto2))

lista = ["manzana", "enero", "c", "Z", "L"]
print(type(lista))

conjunto3 = set(lista)
print(type(conjunto3))

print(conjunto.pop())
print(conjunto.pop())

conjunto3.remove("enero")
print(conjunto3)
conjunto.discard("Enero")
print(conjunto)
print(len(conjunto))
'''
print(conjunto & conjunto2)
print(conjunto | conjunto2)
print(conjunto - conjunto2)
print(conjunto ^ conjunto2)

print(conjunto3.issubset(conjunto2))



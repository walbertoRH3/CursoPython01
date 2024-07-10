diccionario = {1 : 20, 2 : 30, 4 : 40}
diccionario1 = {4 : 51, 6 : 70}

'''
print(diccionario)
diccionario.pop(3)
print(diccionario)
diccionario.clear()
print(diccionario)

print(diccionario.get(2))
diccionario.setdefault(4, 5)
print(diccionario)

diccionario.update(diccionario1)
print(diccionario)
'''

diccionario2 = diccionario.copy()
print(diccionario)
print(diccionario2)




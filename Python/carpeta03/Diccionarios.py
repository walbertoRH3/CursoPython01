'''
diccionario = {"usuario" : "Admin", "Contra" : 1234, "Usuario" : "Juan"}

print(diccionario)
print(type(diccionario))
'''

diccionario = {"Nombre" : "Jose", "Apellido" : "Suarez", "Estatura" : 1.78}
print(diccionario)
print(diccionario.keys())
print(diccionario.values())
print(diccionario["Estatura"])
diccionario["peso"] = "58 kg"
print(diccionario)
diccionario["Estatura"] = 1.75
print(diccionario)
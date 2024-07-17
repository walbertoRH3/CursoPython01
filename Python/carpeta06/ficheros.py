'''
file = open("datos.txt", "r")
#print(file)
lineas = file.readlines()
print(lineas)
file.close() # cerrare el documento.
'''

'''
with open("datos.txt", "r") as archivo:
    lineas = archivo.readlines()
    print(lineas)

for l in lineas:
    print(l.replace("\n", ""))
'''

'''
with open("datos.txt", "r") as archivo:
    contenido  =archivo.read()
    lineas = contenido.split("\n")
    print(lineas)
'''
'''
with open("datos.txt", "r") as archivo:
    contenido  =archivo.read()
    lineas = contenido.split("\n")
    pos = archivo.tell()
    print(pos)
    print("el archivo tiene {} caracteres de longitud".format(pos))
'''
'''
with open("datos.txt", "r") as archivo:
    archivo.seek(7)
    pos = archivo.tell()
    print(pos)
    contenido  =archivo.read()
    lineas = contenido.split("\n")
    print(lineas)
'''
'''
with open("datos.txt", "r") as archivo:
    siguinetes7 = archivo.read(3)
    print(siguinetes7)

    with open("datos.txt", "rb") as archivo:
    print(type(archivo.read()))
'''

with open("datos02.txt", "a") as archivo:
    archivo.write("\nHola Francisco")





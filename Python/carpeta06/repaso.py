'''
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()

print(contenido)
'''
'''
#abriendo el fichero en modo escritura
with open("datos02.txt", "w") as archivo:
    #Escribir datos en el fichero
    archivo.write("canadaMexico")
'''
'''
with open("datos02.txt", "a") as archivo:
    #Anadir datos al final del fichero
    archivo.write("\nEste es mas contenido adicional")

#abrimos el fichero en modo lectura
with open("datos.txt", "r") as archivo:
    #Leer cada linea del fichero
    for linea in archivo:
        print(linea.strip()) #.strip() elimina los espacios en blanco al principio y al final de cada linea

with open("error.txt", "w") as archivo:
    archivo.write("    hola   \n")
    archivo.write("\tmundo\t\t\n")
    archivo.write("    python   ")

with open("error.txt", "r") as archivo:
    for linea in archivo:
        print(f"Original: {linea}")    #mostrar el archivo original
        print(f"Procesado: {linea.strip()}")  #mostrar las lineas procesadas.

'''
try:
    with open("noExiste.txt", "r") as archivo:
        contenido = archivo.read()
except FileNotFoundError:
    print("El archivo que intentas abrir no existe! por favor valida si esta creado en tu ordenador.")
except IOError:
    print("Ocurrio un error de Entrada/Salida")

print("Hola mi programa no dejo de funcionar")





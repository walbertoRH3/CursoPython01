diccionario =  {"Guatemala": "Ciudad de Guatemala", "Honduras": "Tegucigalpa","Nicaragua": "Managua", "Costa Rica": "San Jose", 
                "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid" , 
                "El Salvador" : "San Salvador"}

pais = input("Ingrese un pais para conocer su capital: ")
letra = pais.title() in diccionario

if letra:
    print(diccionario[pais.title()])
else:
    print("El pais no se encuentra en el diccionario")
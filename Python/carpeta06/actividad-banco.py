'''
Problema:

Crea una función que reciba una lista de diccionarios. Cada diccionario representa una transacción bancaria con 
las claves id_transaccion, monto, tipo y fecha. La función debe calcular y retornar el balance final de 
la cuenta bancaria, la cantidad total de transacciones por tipo (deposito o retiro), y un diccionario con las fechas como
 claves y la suma de montos de todas las transacciones realizadas en cada fecha como valores.

La función debe manejar las siguientes excepciones:

* Si alguna transacción no tiene el formato correcto (falta alguna clave), debe ignorar esa transacción y continuar con las demás.
* Si monto no es un número positivo, debe lanzar un mensaje de error específico para esa entrada.
* Si tipo no es un valor válido (deposito o retiro), debe lanzar un mensaje de error específico para esa entrada.
* Si fecha no es una cadena de texto con el formato YYYY-MM-DD, debe lanzar un mensaje de error específico para esa entrada.
'''

def procesar_transaccion(lista_transacciones):
    balance_final = 0
    cantidad_por_tipo = {"deposito" : 0, "retiro" : 0}
    montos_por_fecha = {}

    for transaccion in lista_transacciones:
        try:
            #Verificar que todas las claves esten presentes
            if not all(clave in transaccion for clave in ["id_transaccion", "monto", "tipo", "fecha"]):
                raise KeyError("Falta una clave en el diccionario de la transaccion!")
            
            id_transaccion = transaccion["id_transaccion"]
            monto = transaccion["monto"]
            tipo = transaccion["tipo"]
            fecha = transaccion["fecha"]

            #Verificar que el monto sea un numero positivo
            if not isinstance(monto, (int, float)) or monto <= 0:
                raise ValueError(f"Monto no valido para la transaccion {id_transaccion}")
            
            #verificar que el tipo seq deposito o retiro
            if tipo not in ["deposito", "retiro"]:
                raise ValueError(f"Tipo no valido para la transaccion {id_transaccion}")
            
            #verificar que la fecha sea una cadena de texto con el formato "YYYY-MM-DD"
            if not isinstance(fecha, str) or len(fecha) != 10 or fecha[4] != "-" or fecha[7] != "-":
                raise ValueError(f"Fecha no valida para la transaccion {id_transaccion}")
            
            #calcular el balance final
            if tipo == "deposito":
                balance_final += monto
                cantidad_por_tipo["deposito"] += 1
            elif tipo == "retiro":
                balance_final -= monto # balance_final = balance_final + monto
                cantidad_por_tipo["retiro"] += 1
            
            # actualizar el monto total por fecha.
            if fecha not in montos_por_fecha:
                montos_por_fecha[fecha] = 0
            montos_por_fecha[fecha] += monto

        except KeyError as ke:
            print(f"Error: {str(ke)}")
        except ValueError as ve:
            print(f"Error: {str(ve)}")
        except Exception as e:
            print(f"Error desconocido: {str(e)}")

    return {
        "balance final" : balance_final,
        "Cantidad por tipo" : cantidad_por_tipo,
        "montos por fecha" : montos_por_fecha
    }
    
transacciones = [
    {"id_transaccion" : 1, "monto" : 1250.50, "tipo" : "deposito", "fecha" : "2024-07-10"},
    {"id_transaccion" : 2, "monto" : 250, "tipo" : "retiro", "fecha" : "2024-07-11"},
    {"id_transaccion" : 3, "monto" : -1250.50, "tipo" : "deposito", "fecha" : "2024-07-12"},  #Monto invalido
    {"id_transaccion" : 4, "monto" : 1250.50, "tipo" : "transferencia", "fecha" : "2024-07-13"},  #tipo invalido
    {"id_transaccion" : 5, "monto" : 3250.50, "tipo" : "deposito", "fecha" : "2024-1020"},  #fecha invalida
    {"id_transaccion" : 6, "monto" : 856.50, "tipo" : "deposito", "fecha" : "2024-07-14"},
    {"id_transaccion" : 7, "monto" : 495.50, "tipo" : "retiro", "fecha" : "2024-07-15"}   # falta un clave
]

resultado = procesar_transaccion(transacciones)
print(resultado)

            

            

            



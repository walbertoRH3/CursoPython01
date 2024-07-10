'''
Escribir una función que reciba un número entero positivo y devuelva su factorial.
'''
# 5! = 5*4*3*2*1
def factorial():
    from math import factorial
    num = int(input("Ingresa un numero entero y positivo: "))
    if num > 0:
        print(factorial(num))
    else:
        print("El numero es negativo y no puedo seguir..")

factorial()
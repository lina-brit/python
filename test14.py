def Exponentes (a , l) :
    print(a ** l)
numeración = float(input("No tengo ideas para escribir un numero por favor inserte uno:"))

print(numeración)

from math import  sqrt 
numero = float(input("Por favor inserte un numero:"))
resultado = sqrt(numero)
print(resultado)

#
def multiplicación(k,o):
    print(k * o)
numeritos = float(input("Por favor ingrese um numero para ya no poner yo:"))
numeritos1 = float(input("Por favor ingrese otro numero para ya no poner yo:"))
print(numeritos, numeritos1)

def division (g, h):
    print(g / h)
numero1 = float(input("Por favor incerte un numero:"))
numero2 = float(input("Por favor incerte un numero:"))
print(numero1,numero2)
#Desempaquetar una tupla
numeros= ("cuatro", "nueve", "doce", "diez", "cinco") 
print(numeros)

mi_tupla = (1, 2, 3, 1, 2)
contador = mi_tupla.count(1)
print(contador) 

mi_tupla = (1, 2, 3, 1, 2)
posicion = mi_tupla.index(2)
print(posicion) 

# encapculamiento
class encap:
    def __init__(self):
        self.numero = 0
    def operacion(self):
        print(self. numero + 20)
    def resultado(self):
        return self.numero
ejemplo = encap()
ejemplo.operacion()
ejemplo.numero = 100
print(ejemplo. resultado())



# DESEMPAQUETAR UNA TUPLA
numeros= ("uno", "dos", "tres", "cuatro", "cinco") 
print(numeros)

mi_tupla = (1, 2, 3, 1, 2)
contador = mi_tupla.count(1)
print(contador) 

mi_tupla = (1, 2, 3, 1, 2)
posicion = mi_tupla.index(2)
print(posicion) 

dias = ["lunes", "martes", "miercoles", "jueves", "viernes","sabado","domingo"]


for x in dias:
    print(x)

for x in dias:
    print (x)
    if x == "viernes":
        break

nombre =  "Gimena {}" 
nombres = """lina
noah
willian
lilian
"""
edad = 22
print (nombre. upper())
print (nombre. lower())
print (nombre. replace ("G", "L") )
print (nombre. format(edad))

       


class encap:
    def __init__(self):
        self.numeración = 0
    def operación(self):
        print(self.numero + 40)
    def resultado(self):
        return self.numero
ejemplos = encap()
ejemplos. operación ()
ejemplos.numeración = 112
print(ejemplos.resultado())
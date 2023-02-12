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

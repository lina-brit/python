cantidad = int(input("¿Cuántas veces desea repetir? "))
i = 0

while i < cantidad:
    spaces = " " * (cantidad - i)
    caracter = "❤️" * ((i * 2) + 1)
    print(f'{spaces}{caracter}')
    i += 1
 
 #Pequeño cambio

nombre = ("gimena", "Mauricia", "Hair", "Aristoteles", "Demian", "Luther", )
nombres = """lina 
noah
willian
lilian
"""
for x in nombre:
    print(x)
print (len(nombre))
print (nombres)
print (len(nombres))


print (nombre[0:3])

nombresito = ("tetera","ollas", "sarten", "termo")
numeros = (25, 34,34,77)
valor = (True, False, True)
comvinada = ("tetera", 2, 4, True, False)

print(nombresito)
print (numeros)
print (valor)
print (comvinada)
print(nombresito[2])
print(valor[1:3])
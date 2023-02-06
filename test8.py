cantidad = int(input("¿Cuántas veces desea repetir? "))
i = 0

while i < cantidad:
    spaces = " " * (cantidad - i)
    caracter = "❤️" * ((i * 2) + 1)
    print(f'{spaces}{caracter}')
    i += 1
 
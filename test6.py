# imprimir_piramide(10)

def imprimir_piramide(pisos):
  for i in range(1, pisos+1):
    espacios = " " * (pisos - i)
    asteriscos =  "❤️" * (2 * i - 1)
    print(f'{espacios}{asteriscos}{espacios}')
pisos = int(input("Ingrese los pisos de la pirámide: "))
imprimir_piramide(pisos)
 
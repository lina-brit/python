LaLista = []

def letras(index):
    print(f'[Ingrese el nombre de una letra[{index}]:')
    letra = input()
    LaLista.append(letra) 
    print("has impreso la letra:",LaLista)

i = 0
while i < 7:
    letras(i + 1)
    i = i + 1

from PIL import Image

# Crea una imagen en blanco con el tamaño de 300x200
imagen = Image.new('RGB', (300, 200), color = 'white')

# Guarda la imagen
imagen.save('nombre_imagen.png')
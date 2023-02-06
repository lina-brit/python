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
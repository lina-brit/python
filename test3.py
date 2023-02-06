# tarea crear funcion para imrpimir un cadena que le mande el usuario 
# crear funcion para sumar dos numeros que le mande el usuario
# crear funcion para imprimir una piramide de 10 pisos con ciclo for anidado 

#3 tarea 
def imprimir_piramide(pisos):
    for i in range(1, pisos+1):
        espacios = " " * (pisos - i)
        asteriscos = "❤️" * (2 * i - 1)
        print(espacios + asteriscos)

imprimir_piramide(10)
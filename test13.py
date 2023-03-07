#Wii
def suma(x, y):
    print(x + y)

numero1 = int(input('''introduce un numero natural:
                    por ejemplo 100:'''))
numero2 = int(input("introduce otro numero natural:"))
suma(numero1, numero2)

def multiplicacion(x,y):
    print(x * y)

numero0 = float(input("Introduce un numero decimal:"))
numero3= float(input("Introduce un numero decimal:"))
multiplicacion(numero0, numero3)


numeros= ("uno", "dos", "tres", "cuatro", "cinco") 
print(numeros)

mi_tupla = (1, 2, 3, 1, 2)
contador = mi_tupla.count(1)
print(contador) 

mi_tupla = (1, 2, 3, 1, 2)
posicion = mi_tupla.index(2)
print(posicion) 


def division( a, b):
    print(a / b)
numero4 = int(input("Introduce un numero del 0 a la derecha:"))
numero5 = float(input("Introduce un numero de 0 a la izquierda o la derecha: "))
division(numero4, numero5)

def exponente(b, c):
    print(b ** c)
numero6 = float(input("Introduce un numero decimal o natural:"))
numero7 = float(input("introduce un numero natural o decimal:"))
exponente(numero6, numero7)

def http_error(status):
    match status:
        case 400:
            return "solicitud incorrecta"
        case 404:
            return "Te va a pegar tu mamá"
        case 418:
            return "soy una tetera"
        case _:
            return "algo anda mal en internet"
print (http_error(400))
print (http_error(404))
print (http_error(418))
print (http_error(555))

Diasdelasemana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
for x in Diasdelasemana:
    if x == "Miercoles":
        break
    print(x)

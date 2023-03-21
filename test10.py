#asd

def nombre():
    print("caronte el gato")
    
nombre()

def nombres(text, text2):
    print(text, text2)
nombres("caronte", "gotas")
    

def letras(letra1, letra2, letra3):
    print(letra1, letra2, letra3)

letras ("a","b", "c")

tuplas = ("Adal","Asher", "Edward", "Andy")
print(tuplas)

# agrege una Lista
dias = ["lunes", "martes", "miercoles", "jueves", "viernes","sabado","domingo"]


for x in dias:
    print(x)

for x in dias:
    print (x)
    if x == "viernes":
        break

class Noah:
        def __init__(self, numero):
           self.numero = numero
        def mensaje1(self):
            print("Hola buenas tardes")
        def mensaje2(self):
            print("hola buenas tardes")
        def mensaje3(self):
            print("hola buenas noches")
#Gracias

class Lina(Noah):
    def __init__(self, numero):
        super().__init__(numero)
    def mensaje4(self):
        print("como has hecho tu trabajo")
        print(self.numero + 10)
    def mensaje5(self):
        print("como va la cocina")
    def mensaje6(self):
        print("hasta otro momento")

ejemplo = Lina(10)   
ejemplo.mensaje1()
ejemplo.mensaje5()
ejemplo.mensaje2()
ejemplo.mensaje3()
ejemplo.mensaje6()
ejemplo.mensaje4()

def multiplicación( x, l):
    print(x * l)
numerosos = int(input("Por favor inserte un numero: "))
numerosos1 = int(input("Por favor inserte otro numero:"))
multiplicación( numerosos, numerosos1)
from math import sqrt
numero= int (input("Por favor ingrese un numero:"))
 
resultado= sqrt(numero)
print(resultado)
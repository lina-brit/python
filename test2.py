# esta es una variable
("marte")
# aqui efecutamos la variable  - 
print ("marte")
nombres, nombre1, nombre2, = "carla", "marte", "mauricia"
print (nombres)
print (nombre1)
print (nombre2)
numeros = 72646
print (numeros)
nombre = "mauricia"
print (nombre)
print (type(nombre))
nombre = 724
print (nombre)
print (type(nombre))
numero = 72.4
print (numero)
print (type(numero))
print("hola buenas tardes ¿me puedes dar tu nombre?")
nombrei = input()
print (nombrei)
print (type, (nombrei))
print("hola buenas tardes ¿cual es su numero?")
numero = int(input())
print(numero)

# OPERADORES ARITMETICOS 
x = 35
y = 6

# SUMA " + "
print ("este es el resultado de x + y = ", x + y)

# RESTA " - "
print ("este es el resultado de la resta de x - y =", x - y)

# MULTIPLICACIÓN " * "
print ("este es el resultado de x * y =", x * y)

# DIVISIÓN " / "
print ("este es el resultado de x / y =", x / y )

# PRODUCTO ENTERO DE UNA DIVISIÓN " // "
print ("este es el resultado de x // y =", x // y)

# EXPONENTE " **"
print ("este es el resultado de x ** y =", x ** y)

# OPERADORES COMPARATIVOS
s = 5 
t = 5 
# MAYOR QUE " > "
print (" x es mayor que y", x > y)

# MENOR QUE " < "
print (" y es menor que x", y < x)

# IGUAL A " == "
print (" s es igual a t", s == t)

# NO IGUAL A " != "
print (" s no es igual que y", s != y)

# MAYOR O IGUAL " >= "
print (" s es mayor o igual que t", s >= t)

# MENOR O IGUAL " <= "
print (" s es menor o igual que t ", s >= t) 
numeros = 10
if numeros > 0:
    print (" el numero es positivo")
else:
    print ("el numero es negativo ")

print ("hola introduce un mumero positivo o negativo")
numero = int(input())
if numero > 0:
    print("el numero es positivo")
if numero % 2 == 0:
    print ("este numero es par")
else:
    print("este numero es negativo")

print ("hola introduce un numero negativo o positivo")
numero = int(input())
if numero > 0:
    print ("este numero es positivo")
if numero < 0:
    print ("este numero es negativo")
if numero % 2 == 0: 
    print ("este nuemro es par")

def http_error(status):
    match status:
        case 400:
            return "solicitud incorrecta"
        case 404:
            return "no encontrado"
        case 418:
            return "soy una tetera"
        case _:
            return "algo anda mal en internet"
print (http_error(400))
print (http_error(404))
print (http_error(418))
print (http_error(555))

# FOR ES PARA LISTAS, TUPLAS Y DICCIONARIOS 
dias = ["lunes", "martes", "miercoles", "jueves", "viernes","sabado","domingo"]

# EJEMPLO DE FOR POR LISTAS
for x in dias:
    print(x)

# EJEMPLO DE FOR CON BREAK
for x in dias:
    print (x)
    if x == "viernes":
        break

# EJEMPLO DE FOR CON EXCEPCIÓN
for x in dias:
    if x == "viernes":
        break 
    print (x)

# EJEMPLO DE FOR DE REPETICIÓN 
numero = 5
for x in range(numero):
    print ("hola")
else: 
    print("Fin del ejemplo")

# USO DEL WHILE EN PYTHON 

# REPETICIÓN DE NUMEROS 
numero = 0 
#while numero <= 10:
    #print (numero)
    #numero += 1 

# REPETICIÓN DE NUMEROS CON BREAK
#while numero <= 10:
    #print (numero)
    #if numero == 6:
        #break
    #numero += 1

# REPETICIÓN DE NUMEROS CON CONTINUE 
#while numero < 10:
    #numero += 1
    #if numero == 6 
       #continue 
    #print (numero )

# SUMA DE NUMEROS NATURALES 
numeros = int(input("introduce un numero natural:"))

resul = 0 
contro = 1 

while contro <= numeros:
    resul += contro 
    contro += 1 
print ("la suma de numeros naturales es:", resul)

# CADENAS DE PYTHON 
nombre =  "Gimena {}" 
nombres = """lina
noah
willian
lilian
"""
edad = 22
# TRABAJAR CON UNA CADENA 
for x in nombre:
    print(x)
print (len(nombre))
print (nombres)
print (len(nombres))

# CORTAR CADENAS
print (nombre[0:3])

# CADENAS Y SUS METODOS: UPPER(), LOWER(), REPLACE(), FORMAT()

print (nombre. upper())
print (nombre. lower())
print (nombre. replace ("G", "L") )
print (nombre. format(edad))

#COMO USAR LAS TUPLAS
nombres = ("tetera","ollas", "sarten", "termo")
numeros = (25, 34,34,77)
valor = (True, False, True)
comvinada = ("tetera", 2, 4, True, False)

print(nombres)
print (numeros)
print (valor)
print (comvinada)
#print (len(nombres))

# ACCEDER A ELEMENTOS DE UNA TUPLA
print(nombres[2])
print(valor[1:3])

# ACTUALIZAR UNA TUPLA
x = list(nombres)
x[1] = "Gimena"
nombres = tuple(x)
print(nombres[1])
 
x = list(valor)
x[2] = "False"
valor = tuple(x)
print(valor[2])

#DESEMPAQUETAR UNA TUPLA
#(uno, dos, tres, cuatro, cinco) = numeros
#print(uno)
#print(dos)
#print(tres)
#print(cuatro)
#print(cinco)

# METODOS DE UNA TUPLA COUNT(), INDEX()
# print(numeros.count(2))
# print(valor.index(2))

# LISTAS EN PYTHON 
nombres = ("lucas", "hira", "noali","hair")
numeros = [1, 2, 3, 4, 5,]
varios = [1, 5, 3, "gimena", "lucia", True, False, True]
print (numeros)
print (varios)
print(nombres)
print(len(numeros))

# ACCEDER A ELEMENTOS DE UNA LISTAS
#print(nombres[2])

# CAMBIAR ELEMENTOS DE UNA LISTA
#nombres[1] = "LOL"
#print(nombres)

#METODOS DE LAS LISTAS APPEND(), REMOVE()
#nombres .append("lilian")
#print(nombres)
#nombres .remove("hair")

#DICCIONARIOS EN PHYTON
nombre = {1: "marco", 2:"monica", 3: True, 4:False, 5:"angel"}
print (nombre)
tupla = {"nombre": "marco", "edad": 25,"tup":("marco", 2, 4, "gorge")}
print (tupla)
listas = { 2:"adal", 3: "asher", 4:"amado", 5:"octavio", 6:"andy", 7: "edward"}
print (listas)
#ACCEDER A ELEMENTOS KEYS(), VALUES(), ITEMS()
print (nombre[2])
x = nombre [3]
print(x)

print(listas. keys())
print(tupla .values())
print(nombre. items())

#CAMBIAR ELEMTOS UPDATE()
nombre.update({4:"anna"})
print(nombre) 

#AGREGAR ELEMENTO
nombre.update({7:"Gimena"})
print(nombre) 

#ELIMINAR ELEMTO POP(), POPITEM(), DEL(), CLEAR()
nombre.pop(3)
print(nombre)

#nombre.clear()
#print(nombre)

del nombre[2]
print(nombre)

#FUNCIONES EN PHYTON
def mifuncion():
    print("hello kitty")
mifuncion()

def suma(x, y):
    print(x + y)
#suma(10, 10)
numero1 = int(input("introduce un numero natural:"))
numero2 = int(input("introduce otro numero natural:"))
suma(numero1, numero2)

#RECURSIVIDAD
def factor(numero):
    if numero == 1:
        return 1
    else:
        return (numero * factor(numero-1))
   
factor2 = int(input("introduce un numero para que calcules su factorial:"))
print ("este es el resultado:", factor(factor2))

#USO DE IF
def numeroso(x):
    if x > 0:
        print("tu numero es positivo")
    elif x < 0:
        print("tu numero es negativo")
        print("tu numero es 0")
numero = int(input("introduce un numero negativo o positivo:"))
numeroso(numero)

#USO DE WHILE
def ciclo(x):
    while x <= 10:
        print(x)
        x += 1 
numero = 1
ciclo(numero)

#MODULOS EN PHYTON
#import modulefinder
#def suma(x, y):
    #print(x + y)
#numero1 = int(input("introduce un numero:"))
#nuemro2 = int(input("introduce otro numero:"))

#modulefinder.suma(numero1, numero2)

#def factor(numero):
    #if numero == 1:
     #   return 1
    #else:
        #return (numero * factor(numero-1))
        #factor2 = int(input("introduce un numera para que calcules su factorial:"))
#print ("este es el resultado:",modulefinder. factor(factor2))

#def numeroso(x):
   # if x > 0:
        #print("tu numero es positivo")
    #elif x < 0:
        #print("tu numero es negativo")
        #print("tu numero es 0")
#numero = int(input("introduce un numero negativo o positivo:"))
#modulefinder.numeroso(numero)

#numero = 1
#Modulo.ciclo(numero)

# CLASES Y OBJETOS
#class miprimeraclase:
    # ATRIBUTOS DE INSTANCIA 
   # def __init__(self):
         #  print("hola me llamo hello")
        #metodos
   # def mensaje(self):
        #print("buenas noches")
   # def mensaje2(self):
       # print("hair noa lince XD")
#mensaje = miprimeraclase()
#mensaje.mensaje()
#mensaje.mensaje2()

class clase2:

    def __init__(self, numero):
        self.numero=numero
    def comparar(self):
        if self.numero > 0:
            print("el nuemro es positivo")
        elif self.numero < 0:
            print("el numero es negativo")
        elif self.numero == 0:
            print("el nuemro es cero")
    def ciclo(self):
        while self.numero <= 10:
             print(self.numero)
             self.numero += 1
#ejemplo = clase2(12)
#ejemplo.comparar ()
#ejemplo.ciclo()
ejemplo = clase2(int(input("dame un numero entero:")))
#ejemplo.comparar()
ejemplo.ciclo()

#HERENCIA Y POLIMORFISMO

class padre:
    def __init__(self, numero):
        self.numero = numero
    def mensaje1(self):
        print("hola buenos dias")
    def mensaje2(self):
        print("hola buenas tardes")
    def mensaje3(self):
        print("hola buenas noches")

class hijo(padre):
    def __init__(self, numero):
        super().__init__(numero)
    def mensaje4(self):
        print("como has estado")
        print(self.numero + 10)
    def mensaje5(self):
        print("como va la vida")
    def mensaje6(self):
        print("hasta otra oportunidad")

ejemplo = hijo(10)   
ejemplo.mensaje1()
ejemplo.mensaje5()
ejemplo.mensaje2()
ejemplo.mensaje3()
ejemplo.mensaje6()
ejemplo.mensaje4()

#ENCAPSULAMIENTO
class encap:
    def __init__(self):
        self.numero = 0
    def operacion(self):
        print(self. numero + 20)
    def resultado(self):
        return self.numero
ejemplo = encap()
ejemplo.operacion()
ejemplo.numero = 100
print(ejemplo. resultado())
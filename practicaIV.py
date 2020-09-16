#Practica_IV ---- Lisbeth Pinales Mora
#Ejercicio_1 = Modele tres entidades del mundo real, colocar por lo menos 3
# características distintivas


print("\t\t Tres clases del mundo real >>>\n")


class Persona:
    def __init__(self):
        self.nombre ="Lisbeth"
        self.apellido ="Pinales"
        self.color_de_ojos = "Marron Oscuro"

print(Persona)

class Gato:
    def __init__(self):
        self.raza ="ragdoll"
        self.color ="Negro"
        self.peso_en_lb ="4.5 kilogramos" 

print(Gato)

class Flor:
    def __init__(self):
        self.tipo ="Orquideas"
        self.color ="Rosa"
        self.tamaño ="13.4 metros" 

print(Flor)

#Ejercicio_2 = Crear una clase llamada Estudiante con un campo llamado promedio, el cual
#solo podrá ser accedido mediante un metodo. El valor del promedio no puede
#estar por encima de 100 que es la nota máxima.


print("\t\t Class Student - Average >>>\n")

class Estudiante:
    def __init__ (self):
        print(">>> Promedio del Estudiante")
    def show_average (self, mensaje):
        print(mensaje)

Student1 = Estudiante()

Student1.show_average("El promedio del estudiante es de 96.2")


#Ejercicio_3 = Hacer una clase llamada Aritmética, que contenga métodos para cada una de
#las operaciones aritméticas básicas.



print("\t\t Aritmetica Class >>>\n")


class Aritmetica:
    def __init__ (self):
        print("Operaciones basicas")
    def mostrar_operaciones (self, mensaje):
        print(mensaje)

Adicion = Aritmetica()
Sustracción = Aritmetica()
Multiplicacion  = Aritmetica()
Division = Aritmetica()

Adicion.mostrar_operaciones(">>> Adicion: Consiste en combinar o añadir dos números o más para obtener una cantidad final")
Sustracción.mostrar_operaciones(">>> Sustraccion: Hace referencia a eliminación de objetos de una colección")
Multiplicacion.mostrar_operaciones(">>> Multiplicacion: Consiste en sumar un número tantas veces como indica otro número")
Division.mostrar_operaciones(">>> División: Es una operación binaria que a dos números asocia el producto del primero por el inverso del segundo")

#Ejercicio_4 = Cree una clase llamada Personaje con los métodos de instancia MoverArriba,
#MoverAbajo, MoverDerecha y MoverIzquierda. Cree una clase llamada Mario y
#otra clase llamada Koopa que herede las funcionalidades de la clase Personaje.


print("\t\t Ejercicio de Herencia Python >>>\n")

class Personaje:
    def __init__(self):
        self.MoverArriba ="MoverArriba"
        self.MoverAbajo ="MoverAbajo"
        self.MoverDerecha ="MoverDerecha" 
        self.MoverIzquierda ="MoverIzquierda" 

class Mario:
    
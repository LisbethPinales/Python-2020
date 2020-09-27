#Modulos en Python: Un archivo en Python;
#Ejemplo: misfunciones.py

#Importar modulos en otro modulo

#Las constantes se ponen en MAYUSCULAS. El concepto de constante se refiere a que el valor no varia, no se cambian su valor.

import practicaI #Para llamar todas las fuciones 
from practicaI import cualquier variable #para llamar una funcion en especifico
from practicaI import * #para llamar todas las funciones

#IMPORTANDO PAQUETES
#1. Crear una carpeta. Ej: Mismodulos
#2. Crear un archivo dentro de esa carpeta con el nombre: __init__.py

class Estudiante:
    def__init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

e =  Estudiante("Juan", "Perez")

#Si intento importar esa clase en otro modulo, me saldra, pero si intento ejecutar la variable Estudiante en ese otro archivo
#no me traera nada porque no conoce esa clase. HAY QUE IMPORTAR

#COLECCIONES

#Si necesitamos 4 calificaciones, teniamos que crear las variables una por una y asignarles un valor. Python permite que podriamos crear 
#un GitHub para almacenar un conjunto de datos bajo un mismo identificador:

#1. Lista: Son objetos y tienen una serie de metodos y atributos como append (para agregar un elemento a la lista) o remove (para eliminar)
#las variables en singular y las colecciones en plurar

notas = [90,80,70,85]
#para tomar un valor de la coleccion debemos utilizar un indice con la posicion del numero. La primera posicion es 0, luego la 1, etc

print(notas[2])

#tambien puedo cambiarle el valor a la calificacion
notas[2] = 75
print(notas[2])

#BLUCKER FOR: para hacer una lista de las variables, y aparezcan de forma individual en la pantalla}

for nota in notas:
    print(nota)

#2. Duplas = Es similar a la Lista, pero no se puede modificar, esa es la diferencia esencial, ES INMUTABLE, no se puede alterar.

notas_tupla = ("90", "80", "7")

for nota in notas_tupla:
    print(nota)
print(notas_tupla[1])

#3. Diccionarios = Permite definir una estructura de datos, con un formato clave:valor, que se refiere a una palabra clave y una definicion

usuario = {"usuario": "ffulgencio", "clave": "123456"}
print(usuario["usuario"])

#esto se utiliza mucho con coleccion de datos. Json es como un diccionario

# conectar base de datos en py con sqlite3
#1. importar el modulo con el que trabajaremos
#2. crear una conexion a la bd
#3. crear una variable intermedia que nos permita emviar consultas a la bd
#4. cerrar la conexion 

"VER VIDEO DE 15 MINUTOS QUE PUBLICARA EL MAESTRO"
"ESTO ES SQL NO PYTHON"

import sqlite3
conn = sqlite3.connect("mydb.db")
cursor = conn.cursor()

query1 = ""
CREATE TABLE Estudiantes (nombre text, apellido text):

query2 = " "
INSERT INTO Estudiantes VALUES ("Juan", "Jimenez"):
" "

query3 = " "
SELECT nombre, apellido FROM Estudiantes:
" "

cursor.execute(query3)

result = cursor.fetchone()

 # PASO 4. VALIDAR LOS CAMBIOS

conn.commit()

#PASO 5. CERRAR LA CONEXION
conn.close



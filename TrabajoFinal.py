# TRABAJO FINAL - Hacer un programa que funcione como agenda telefónica

# El programa debe precargar 10 contactos al iniciar.

# Al iniciar el programa el usuario debe tener opciones que le permitan agregar, buscar,
#... actualizar y borrar un contacto. También una opción que le permita listar todos los contactos.

#Cada contacto debe tener al menos 3 campos Id, nombre y teléfono. (puede agregar todos los que quiera)

#El programa debe permitir buscar por id y por nombre.

#Cuando elija agregar contacto debe de pedir si desea agregar otro.

#Después de cada opción debe volver al menú.

#El programa solo terminara cuando el usuario elija salir.


import csv
import itertools
import re

import sqlite3
conn = sqlite3.connect("miagenda.db")
cursor= conn.cursor()
conn.close()

#clases

class Contacto:
    nuevoId = itertools.count()
    def __init__(self,nombre,telefono,empresa):
        self.codigo = next(self.nuevoId)
        self.nombre = nombre
        self.telefono = telefono
        self.empresa = empresa
class Agenda:
    def __init__(self):
        self.contactos=[]
    def ordernarNombre (self):
        self.contactos.sort(key=lambda contacto: contacto.nombre)
    def añadir (self, nombre, telefono, empresa):
        contacto = Contacto (nombre, telefono, empresa)
        self.contactos.append(contacto)
    def mostrarTodos(self):
        self.submenuOrden()
        for contacto in self.contactos:
            self.imprimeContacto(contacto)
    def buscar(self, textoBuscar):
        encontrado = 0
        for contacto in self.contactos:
            if(re.findall(textoBuscar,contacto.nombre)) or (re.findall(textoBuscar, contacto.codigo)):
                self.imprimeContacto(contacto)
                encontrado =encontrado + 1
                self.submenuBuscar(contacto.codigo)
        if encontrado  == 0:
            self.noEncontrado()
    def borrar(self,codigo):
        for contacto in self.contactos:
            if contacto.codigo  == codigo:
                print(" >>> ¿Desea borrar el contacto? (s/n)")
                print("---*---*----*")
                opcion = str(input(""))
                if opcion== "s" or opcion== "S":
                    print(" >>> Contacto eliminado exitosamente")
                    del self.contactos(codigo)
                elif opcion  == "n" or opcion=="N":
                    break
    def modificar(self,codigo):
        for contacto in self.contacto:
            if contacto.codigo ==codigo:
                del self.contactos[codigo]
                nombre= str(input("Digite el nombre >>> "))
                telefono= str(input("Digite el número telefonico >>> "))
                empresa= str(input("Digite su compañia o empresa movil >>> "))
                Contacto = Contacto(nombre.capitalize(),telefono.capitalize(),empresa.capitalize())
                self.contactos.append(contacto)
                break
    def submenuBuscar (self,codigo):
        print("---*---*----*")
        print(" ¿Quieres modificar el contacto o desea borrarlo? >>>")
        print("---*---*----*")
        opcion=str(input(""))
        if opcion == "n" or opcion== "N":
            self.modificar(codigo)
        elif opcion== "b" or opcion == "B":
            self.borrar(codigo)
        else:
            print("Continuamos sin realizar ninguna modificacion")
    def submenuOrden(self):
              print("---*---*----*")
              print("¿Quieres ordenar por nombre o por código? >>> ")
              print("---*---*----*")
              opcion= str(input(""))
              if opcion == "n" or opcion == "N":
                  self.ordernarNombre()
                
    def modificar_contacto(self):
        with open("miagenda.csv", "w") as fichero:
            escribir=csv.writer(fichero)
            escribir.writerow(("codigo", "nombre","telefono", "empresa"))
            for contacto in self.contactos:
                escribir.writerow((contacto.codigo, contacto.nombre, contacto.telefono, contacto.empresa))

    def imprimeContacto (self, contacto):
        print("---*---*----*")
        print("---*---*----")
        print("Codigo: {}". format(contacto.codigo))
        print("Nombre: {} ". format(contacto.nombre))
        print("Telefono: {}". format (contacto.telefono))
        print("Empresa:{} ". format (contacto.empresa))
        print("---*---*----")
    def noEncontrado(self):
        print("---*---*----*")
        print("Contacto no encontrado >>>")
        print("---*---*----*")
         
    def ejecutar():
         agenda =Agenda()
         try:
             with open("miagenda.csv", "r") as fichero:
                 lector = csv.DictReader(fichero, delimiter="," )
                 for fila in lector:
                     agenda.añadir(fila["nombre"].capitalize(), fila["telefono"])

         except:
             print("Error al abrir el fichero >>> ")
    
def menu():
    opcion = 0
    while opcion != 6:
         print("\t>>>Bienvenido a su agenda telefonica\n")
         print("1. Agregar nuevo contacto")
         print("2. Listar todos los contactos")
         print("3. Buscar contacto agregado")
         print("4. Actualizar contactos agregados")
         print("5. Eliminar contacto agregado")
         print("6. Salir de menú")
         opcion = int(input("Seleccione una opcion >>> "))
         clear()

         if menu == "1":
            agenda.mostrarTodos()
         elif menu == "2":
            texto = str(input("Escribe el texto a buscar en contactos >>> "))
            agenda.buscar(texto.capitalize())
            agenda.modificar_contacto()
         elif menu== "3":
            nombre= str(input("Digite el nombre: >>> "))
            telefono= str(input("Digite el número telefonico: >>> "))
            empresa= str(input("Digite su compañia o empresa movil: >>> "))
            agenda.añadir(nombre.capitalize(),telefono.capitalize(), empresa.capitalize())
            agenda.grabar()
         elif menu== "0":
            print("Hasta pronto")
            agrenda.grabar()
            break
         else:
            print("Opcion no valida")
if __name__=="__main__":
    ejecutar()











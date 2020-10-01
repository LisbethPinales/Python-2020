# #Usando lo aprendido hasta ahora:
# Hacer un programa con acceso a base de datos
# que sirva como una agenda telefónica.
# Debe tener un menu que permita:
# 1 – agregar nuevo contacto
# 2 – Listar todos los contactos
# 3 – Buscar contactos por nombre o numero de teléfono
# 4 – Actualizar un contacto
# 5 – Eliminar un contacto
# 6 – Salir
# Al agregar un nuevo contacto, debe validar que el contacto no exista previamente. Si existe debe dar un
# mensaje notificando al usuario.
# Al terminar de agregar un contacto debe preguntar si desea agregar otro

import sqlite3
conn = sqlite3.connect("miagendatelefonica.db")
cursor= conn.cursor()
conn.close()

class Database:
     def __init__(self):
          self.connection = sqlite3.connect(
               host= "localhost",
               user= "LisbethPinales",
               password= "2020",
               db="miagendatelefonica"

         )

          self.cursos = self.conexion.cursor()


     def add_contact (self,id,contacto,Telefono,Direccion):

          sql = "INSERT INTO miagendatelefonica (ID,contacto,telefono) VALUES ('{}','{}','{}','{}','{}')".format(ID,contacto,telefono)

          try:
              self.cursos.execute(sql)
              self.connection.commit()
              self.cursos.close()
              self.connection.close()
              print(">>> Contacto registrado exitosamente")

          except Exception:
              print(">>> Contacto invalido")

              raise



     def listar_contact(self):
         sql = "SELECT ID,contacto,telefono FROM miagendatelefonica"

         try:
             self.cursos.execute(sql)
             miagendatelefonica = self.cursos.fetchall()

             for mostrar in miagendatelefonica:
                 print("ID:", mostrar[0])
                 print("Contacto:", mostrar[1])
                 print('Telefono:', mostrar[2])
                 print('----------\n')


         except Exception:
             raise



     def search_user(self,contacto):

         sql= "SELECT ID, contacto, telefono FROM miagendatelefonica WHERE contacto = '{}' ".format(contacto)

         try:

            self.cursos.execute(sql)
            miagendatelefonica = self.cursos.fetchone()

            print("ID:", miagendatelefonica[0])
            print("Contacto:", miagendatelefonica[1])
            print("Telefono:", miagendatelefonica[2])
            self.cursos.close()
            self.connection.close()



         except Exception:
            print(">>> Este contacto no existe en su agenda telefonica")
            raise




     def update_contact (self,contacto,Telefono):
         sql = "UPDATE miagendatelefonica SET telefono = '{}' WHERE contacto = '{}'".format(contacto, Telefono)
         try:
             self.cursos.execute(sql)
             self.connection.commit()
             self.cursos.close()
             self.connection.close()

         except Exception:
            print(">>> Intente mas tarde")
            raise



     def remove_contact(self,contacto):
         sql = " REMOVE FROM miagendatelefonica WHERE contacto = {}".format(contacto)

         try:
             self.cursos.execute(sql)
             self.connection.commit()
             self.cursos.close()
             self.connection.close()
             print(">>> Contacto eliminado")

         except Exception:
             print(">>> Favor ingresar un contacto valido")
             raise


def clear():
    if os.name == "posix":
        os.system("cls")
    elif os.name == ("ce","nt","dos"):


        os.system("clear")


def menu():
    opcion = 0
    while opcion != 6:
         print("\t>>>Bienvenido a su agenda telefonica\n")
         print("1. Agregar nuevo contacto")
         print("2. Listar todos los contactos")
         print("3. Buscar contacto agregado")
         print("4. Actualizar contactos agregados")
         print("5. Eliminar contacto agregado")
         print("6. Salir del menú")
         opcion = int(input("Seleccione una opcion >>> "))
         clear()
         
         print("\n")

#funcionalidad a las funciones
         
         database = Database()
         if opcion == 1:
             agregar = "no"
             while agregar != "no":

                 id= str(input("Ingrese el ID del contacto >>> "))
                 contacto = str(input("Digite el nombre del contacto >>> "))
                 telefono = str(input("Indique el número telefonico"))
                 database.add_contact (ID,contacto,telefono)
                 print("\tContacto Agregado\n")
                 agregar = input("¿Gustaría agregar un nuevo contacto?")
                    



         elif opcion == 2:
             database.listar_contact()
             print("\n")


         elif opcion == 3:
            contacto = str(input(" Inserte el contacto que desea buscar >>> "))
            print("\n")
            database.search_user(contacto)



         elif opcion == 4:
             clear()
             contacto = str(input(" Inserte el contacto que desea buscar >>> "))
             database.search_user(contacto)
             clear()
             print("\n")


             telefono = input('Telefono: ')

             database.update_contact(telefono , contacto)


         elif opcion == 5:

             id = str(input(" Inserte el contacto que desea eliminar >>> "))
             database.remove_contact(contacto)
             print("\n")


         elif opcion == 6:
             print(">>> Gracias por utilizar los servicios de su agenda telefonica móvil ")



menu()
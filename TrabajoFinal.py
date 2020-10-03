#Grupo 3:
#Lisbeth Pinales
#Luis Mercedes



import csv
import itertools
import re

import sqlite3
conn = sqlite3.connect("miagenda.db")
cursor= conn.cursor()
conn.close()

class connexionDB:
    def __init__(self):
        conexion = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "melenciano1629",
            db= "agenda"

        )

        self.cursor = conexion.cursor()


    def Agregar(self,nombre,telefono,compañia,direccion):

          sql = "INSERT INTO contacto (nombre,telefono,compañia,direccion) VALUES ('{}','{}','{}','{}')".format(nombre,telefono,compañia,direccion)

          try:
              self.cursos.execute(sql) 
              cout = self.cursor.rowcount
              self.conexion.commit()

              return cout
              self.cursor.close()
              self.conexion.close()
             

          except Exception as err:
              self.conexion.rollback()
              return err


    def registro_repetido(self,nombre,telefono):

         sql = "SELECT * FROM contacto WHERE nombre = '{}' AND telefono = '{}'".format(nombre,telefono)

         self.cursor.execute(sql)
         count = self.cursor.fetchall

         if count == 0:
             print("El nombre o el telefono ya existe.!!!")
             return 1
         else:
             return 0 

           

     #Metodo listar todos los contactos
    def listar_contactos(self):
         sql = 'SELECT idcod,nombre,apellido,telefono,direccion FROM contacto'

         try:
             self.cursos.execute(sql)
             contacto = self.cursor.fetchall()

             for mostrar in contacto:
                 print('ID:', mostrar[0])
                 print('Nombre:', mostrar[1])
                 print('telefono:', mostrar[2])
                 print('compañia:', mostrar[3])
                 print('Direccion:', mostrar[4])
                 print('----------\n')


         except Exception as err:
             return err




    def welcome_registro(self):

         sql = " SELECT * FROM contactos LIMIT 10"

         try:
             self.cursor.execute(sql)
             contacto = self.cursor.fetchall()


             for mostrar in contacto:
                 print('ID:', mostrar[0])
                 print('Nombre:', mostrar[1])
                 print('telefono:', mostrar[2])
                 print('compañia:', mostrar[3])
                 print('Direccion:', mostrar[4])
                 print('----------\n')
            
             return True
         
             self.cursor.close()
             self.conexion.close()
             

         except Exception as err:
             return err

     #Metodo mostrar
    def Mostrar(self,id):

         sql= "SELECT id, nombre,telefono,compañia, direccion FROM contacto WHERE id = '{}' ".format(id)

         try:

            self.cursos.execute(sql)
            contacto = self.cursos.fetchone()

            print('ID:', contacto[0])
            print('Nombre:', contacto[1])
            print('Apellido:', contacto[2])
            print('Telefono:', contacto[3])
            print('Direccion:', contacto[4])
            self.cursor.close()
            self.conexion.close()
            return True



         except Exception as err:
             self.conexion.rollback()
             print("EL ID no es valido")
             return err
            



     #metodo Actualizar
    def Actualizar(self,nombre,telefono,idcod):
         sql = "UPDATE contacto SET nombre = '{}' AND  telefono = '{}'  WHERE id = '{}' ".format(nombre, telefono, idcod)
         try:

             self.cursor.execute(sql)
             self.conexion.commit()
             print("El registro se actualizo correctamente")
          
             self.cursor.close()
             self.conexion.close()

         except Exception as err:
             self.conexion.rollback()
             return err

             


     #metodo eliminar
    def Eliminar(self,codigoid):

         sql = " DELETE FROM cursor WHERE id = {}".format(codigoid)

         try:
             self.cursor.execute(sql)
             self.conexion.commit()
             print('EL REGISTRO SE HA ELIMINADO CORRECTAMENTE!!!')
             return True
         
             self.cursor.close()
             self.conexion.close()
             

         except Exception as err:
             self.conexion.rollback()
             print('EL REGISTRO NO SE PUDO ELIMINAR!!!')
             return err


from conexionMySQL import connexionDB


#Funcion de menu principal.
def menu_principal():

     opcion = 0
     while opcion != 6:
         print('\tWELCOME AGENDA TELEFONICA\n')

         print('1.AGREGAR NUEVO CONTACTO.')
         print('2.MOSTRAR TODOS LOS CONTACTOS.')
         print('3.BUSCAR CONTACTO.')
         print('4.ACTUALIZAR CONTACTO.')
         print('5.ELIMINAR UN CONTACTO.')
         print('6.SALIR.')
         opcion = int(input("ELEGIR OPCION: "))
        
         
         print("\n")


         
         database = connexionDB()
         if opcion == 1:

             agregar = ""
             while agregar != "no":

                   
                     nombre = str(input('Digite su nombre: '))
                     telefono = str(input('Diga cual es su Telefono: '))
                     compañia =  str(input('Cual es la compañia de su telefono: '))
                     direccion = str(input('Cual es su direccion: '))

                     database.registro_repetido(nombre,telefono)
                     if database.registro_repetido (nombre,telefono) == 1:
                        return 2

                     else:
                         database.Agregar(id,nombre,telefono,compañia,direccion)

                     agregar = input("DESEA AGREGAR OTRO REGISTRO(SI/NO)?: ")
                     agregar.lower()
           
                 

       
         elif opcion == 2:
             database.listar_contactos()
             print("\n")


         elif opcion == 3:
            codigoid= (input('introduzca el id del Registro que desea ver: '))
            print("\n")
            database.Mostrar(codigoid)


         elif opcion == 4:
             
                          
             idcod = input('Digita id del registro a Actualizar: ')
             database.Mostrar(idcod)
             print("\n")
             nombre = input(' Actualizar nombre: ')
             telefono = input(' Actualizar Telefono: ')
             
             
             database.Actualizar(nombre,telefono,idcod)
            


         elif opcion == 5:

             codigo = str(input('INTRODUZCA EL ID DEL REGISTRO: '))
             eliminar = database.Eliminar(codigo)
           
            
             print("\n")


         elif opcion == 6:
             print("Adios!!!")

         else:
             print("OPCION NO VALIDA!!!")

def precargar():
     database = connexionDB()
     print("bienvenidos a tu Agenda Telefonica, estos son los 10 contactos\n")
     database.welcome_registro()



precargar()
menu_principal()

SystemExit

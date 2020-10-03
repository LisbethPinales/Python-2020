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
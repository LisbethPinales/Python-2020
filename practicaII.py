#Practica_2   ---- Lisbeth Pinales Mora

#Ejercicio_1 = Realizar un programa que solicite al usuario un número indeterminado de números (mientras se tecleen números que no sean cero). 
#Al salir el programa debe dar en pantalla el total de números dados y la suma de ellos.

print("\t\tIndeterminate numbers\n")

userno1 = int(input("Ingrese un numero indeterminado de numeros"))
userno2= int(input("Ingrese otro numero"))
userno3 = int(input("Ingreso un ultimo numero"))

c = userno1, userno2, userno3
print(c)
suma= lambda userno1, userno2, userno3 : print(userno1 + userno2 + userno3)
suma(userno1, userno2, userno3) 

#Ejercicio_2 = Realizar un programa que presente un menú con las siguientes opciones
#... 1- Convertir grados a Celsius a Fahrenheit
#...2- Convertir dólar a pesos
#...3- Convertir metros a pies
#...4- Salir
#...Cada vez que finalice una de estas acciones debe regresar al menú. El programa solo finalizará cuando el usuario elija la opción salir.

print("\t\tConversor Program\n")

opcion = 0
while opcion != 4:
    print("1. Convertir de grado a celsius a Fahrenheit")
    print("2. Convertir de Dolar a pesos")
    print("3. Convertir de metros a pies")
    print("4. Salir\n")
    opcion = int(input("Elegir opcion:"))

    if opcion == 1:
        cl = int(input("Introduza cantidad de celsius: "))
        fr = (cl * 1.8) + 32
        print(" La cantidad de Fahrenheit es igual a >>>: " + str(fr))

    elif opcion == 2:
        dll = int(input("Digite la cantidad de Dolares que desea convertir a pesos: "))
        pss = (dll * 58.52)
        print("Convertido a pesos, es igual a >>>: " + str(pss))

    elif opcion == 3:
        mt = int(input("Digite la cantidad de metros que desea convertir a pies: "))
        pies = (mt * 3.281)
        print("Convertido a pies, es igual a >>>: " + str(pies))


else :
    print("\tHasta Luego")
    SystemExit

#Ejercicio_3 = Hacer un programa que genere las tablas de multiplicar de los números múltiplos de 5 que hay entre 1 y 1000

print("\t\Multiplication Table\n")
number_random = 5

for i in range(1,1001):
    print(f"{i} * {number_random} = {i * number_random}")

#Ejercicio_4 = Realizar un programa que reciba por teclado el sueldo de un empleado y le
#... aplique los cálculos de ISR (ver tabla DGII), ARS, y AFP (investigar porcentajes)

print("\t\tISR Calculator with AFP & ARS discounts monthly\n")

limit1 = 416220.00
limit2 = 624329.00
limit3 = 867123.00

wage = float(input("Digite su sueldo mensual"))
anual_wage = wage * 12
isr = 0
afp = 0
sfs = 0

if anual_wage <= limit1:
    print("Exempt ISR")
    afp1= anual_wage * 0.0287
    afp =  anual_wage - afp1
    sfs1= anual_wage * 0.0304
    sfs = anual_wage - sfs1
elif anual_wage <= limit2:
    surplus = anual_wage - limit1
    isr = surplus * 0.15
    afp1 = anual_wage * 0.0287
    afp = anual_wage - afp1
    sfs1= anual_wage * 0.0304
    sfs = anual_wage - sfs1
elif anual_wage <= limit3:
    surplus = anual_wage - limit2
    isr = 31216.00 + (surplus * 0.20)
    afp1 = anual_wage * 0.0287
    afp = anual_wage - afp1
    sfs1= anual_wage * 0.0304
    sfs = anual_wage - sfs1
else:
    surplus = anual_wage - limit3
    isr = 79776.00 + surplus * 0.25
    afp1 = anual_wage * 0.0287
    afp = anual_wage - afp1
    sfs1= anual_wage * 0.0304
    sfs = anual_wage - sfs1

print(isr / 12)
print(afp/12)
print(sfs /12)

#NOTA: Entendiendo que ARS hace referencia a SFS (Seguro Familiar de Salud), la cual es reglamentada en la Ley 87-01.

#5-Cree una aplicación de cajero automático para el banco ABC. El cajero tendrá un
# límite de billetes descrito a continuación: 9 de 1000, 19 de 500, 99 de 100
# El cajero debe solicitar Banco y monto a retirar. Si el banco es ABC el limite de
# retiro son 10,000 y 2000 pesos por transacción en caso contrario.
# El cajero debe informar si el monto solicitado no puede ser dispensado o si
# excede el límite de transacción. Y debe hacer la distribución de los billetes de
# acuerdo al monto. Por ejemplo, si el usuario solicita 3,900 y hay disponibilidad en
# todos los billetes, el cajero debe dispensar 3 billetes de mil, 1 de quinientos y 4 de
# cien.


print("\t\tCajero Automatico Banco ABC Av. Winston Churchill\n")

import random
user = "30018"
pssw = "8888"
saldo = random.randint(0,100000)
saldo1= random.randint(0,10000)
cont = 0
connected = bool

while cont < 3:
    us= input("Digite su usuario")
    ps = input("Digite su contraseña")
    if us == user and pssw == ps:
        print("Bienvenido a su Cajero Automatico ABC")
        connected= True
        break
     
    else:
        cont= cont + 1
        print("Usuario y contraseña no compatible")
        connected = False
    
while connected == True:
    print("Seleccione la opcion que desea utilizar")
    print("1. Retiro")
    print("2. Sin habilitar")
    eleccion = int(input("Ingrese opcion"))
    if eleccion == 1:
        monto= int(input("Ingrese monto a retirar:"))
        saldo= saldo - monto
        print("Estimado cliente, usted ha retirado" , monto)

        if monto > 10000:
             print(">>>Monto excedido")
        if monto %2 == 0:
             print(">>>Billetes no disponibles. Monto no puede ser dispensado")
       
        print("|Gracias por utilizar los servicios de su BANCO ABC|")

        SystemExit
#Practica_2
#Ejercicio_1 = Realizar un programa que solicite al usuario un número indeterminado de números (mientras se tecleen números que no sean cero). 
#Al salir el programa debe dar en pantalla el total de números dados y la suma de ellos.


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

ans = True
while ans:
    print("1.Convertir grados a Celsius a Fahrenheit , 2. Convertir dolar a pesos, 3. Convertir metros a pies, 4. Salir")

ans= input("¿En que te puedo ayudar?")

    if ans= "1":
        print("1.Convertir grados a Celsius a Fahrenheit , 2. Convertir dolar a pesos, 3. Convertir metros a pies, 4. Salir")
    elif ans == "2":
        print("1.Convertir grados a Celsius a Fahrenheit , 2. Convertir dolar a pesos, 3. Convertir metros a pies, 4. Salir")
    elif ans== "3"
        print("1.Convertir grados a Celsius a Fahrenheit , 2. Convertir dolar a pesos, 3. Convertir metros a pies, 4. Salir")
    elif ans == "4"
        print("Gracias por su visita")
   
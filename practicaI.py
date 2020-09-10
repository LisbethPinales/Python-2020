#Practica_1 
#Ejercicio_1 = Escriba en pantalla el tipo de dato que retorna la expresión 4 < 2
result = 4<2
print(result)

#Ejercicio_2 = Almacene en una variable el nombre de una persona y al final muestre en la consola el mensaje: Bienvenido [nombrePersona]
name = "Ezequiel Hibrea"
print("Bienvenido", name)

#Ejercicio_3 = Evalúe si un número es par o impar y muestre en la consola el mensaje.
#Suponiendo que necesito saber sí 5,9,113,120 y 1568 son números pares o impares, tenemos la siguiente sintaxis
number1 = 5
number2 = 9 
number3 = 113
number4 = 120
number5 = 1568
if number1 % 2  == 0:
    print("Par")

if number2 % 2  == 0:
    print("Par")

if number3 % 2  == 0:
    print("Par")

if number4 % 2  == 0:
    print("Par")

if number5 % 2  == 0:
    print("Par")

#Ejercicio_4 = Almacene dos números y evalúe si el primero es mayor que el segundo. El resultado debe verse en la consola.
#Considerando dos números al azar

No1 = 6780
No2 = 7885

result_exer4 = No1 > No2
print(result_exer4)

#Ejercicio_5 = Convierta dólares a pesos

usd = 1560
usd1 = 560
rate_do = 58.41

result_exer5 = usd * rate_do
print(result_exer5)

result_exer5b = usd1 * rate_do
print(result_exer5b)

#Ejercicio_6 = Convierta grados celsius a Fahrenheit

celsius = 52
celsiusb = 89
fa = 32

result_exer6 = celsius * 9/5 + fa
print(result_exer6)

result_exer6b = celsiusb * 9/5 + fa
print(result_exer6b)

#Ejercicio_7 = Almacene cuatro notas 90,95,77, 92 y las promedie. Al final debe decir su calificación en letras A, B,C,D, E ó F.
qualification1= 90
qualification2 = 95
qualification3 = 77
qualification4 = 92
summary = qualification1 + qualification2 + qualification3 + qualification4
print(summary/4)

#considerando que, average 90 - 100 = A ; 80 - 89 = B ; 70 - 79 = C ; qualificationX < 69 = D

if qualification1 == 90:
    print("A")

if qualification2 == 95:
    print("A")

if qualification3 == 77:
    print("C")

if qualification4 == 92:
    print("A")

#Ejercicio_8 = Que almacene monto, cantidad de cuotas, y porcentaje de interés anual de un préstamo y calcule la cuota mensual. (Amortizar mediante el sistema francés)

mount = 100000
float_1 = 0.09
print (float_1)
n = -5

resultdenominador = 1 - (1 + float_1)**n 
print(resultdenominador)

resultcociente = float_1 / resultdenominador
print(resultcociente)

resultado_cuota_anual = mount * resultcociente
print(resultado_cuota_anual)

resultado_cuota_mensual = resultado_cuota_anual / 12
print(resultado_cuota_mensual)

#nota: el cliente debe abonar una cuota de DOP$ 2,142.44 mensuales, pagadero en 60 (o 5 años) contribuciones cada mes, al 9% anual
#... con la finalidad de amortizar un prestamo tomado de DOP$ 100,000.00 (según resultados de fórmula Amortización sistema francés)

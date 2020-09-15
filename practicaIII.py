#Practica_III ---- Lisbeth Pinales Mora
#Ejercicio_1 = Hacer una función que potencie un número x a la y

print("\t\t Ejercicio numero 1\n")

def potencia (base_number, exponente): 
    result = 1

    for i in range(exponente):
        result *= base_number


    return result

#example
print(potencia(3,3))
print(potencia(3,5))

#Ejercicio_2 = Realizar una función que pida por pantalla un número del 1 al 10 y muestre por pantalla el número escrito en letras.

print("\t\t Ejercicio numero 2\n")

def convert_number_toletters (toletters):

    number = [ 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    letters = ["Mil", "Novecientos", "Ochocientos", "Setecientos", "Seiscientos", "Quinientos", "Cuatrocientos", "Trecientos", "Doscientos", "Cien", "Noventa", "Ochenta", "Setenta", "Sesenta", "Cincuenta", "Cuarenta", "Treinta", "Veinte", "Diez", "Nueve", "Ocho", "Siete", "Seis", "Cinco", "Cuatro", "Tres", "Dos", "Uno"]
    letter =  " "
    i = 0


    while toletters > 0:
        for _ in range(toletters // number [i]):
            letter += letters [i]
            toletters -= number[i]

        i += 1 

    return letter

print(convert_number_toletters(1050))
print(convert_number_toletters(54))


#Ejercicio_3 = Hacer una función que reciba un año como argumento y retorne verdadero si es bisiesto.

print("\t\t Ejercicio numero3\n")

def bisi (year): 
    if year %400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year= 2020
print("¿Es cierto que año %i es bisiesto?: %s " % (year, bisi (year)))
year= 2017
print("¿Es cierto que año %i es bisiesto?: %s " % (year, bisi (year)))


#Ejercicio_4 = Crear una función que evalúe dos números y retorne verdadero si ambos números son iguales.

print("\t\t Ejercicio numero 4\n")

def no_iguales (numero_cualquiera, otro_numero):
    if numero_cualquiera == otro_numero:
        return True
    else:
        return False
    

print(no_iguales(4,5))
print(no_iguales(5,5))

#Ejercicio_5 = Un número palindrómico se lee igual en ambos sentidos. El palíndromo más grande hecho del producto de 
# dos números de 2 dígitos es 9009 = 91 × 99.
# Cree una función que encuentre el palíndromo más grande hecho del
# producto de dos números de 3 dígitos.

print("\t\t Ejercicio numero 5\n")

def esPalindrom(numero):
    if str(numero)==str(numero)[::-1]:
        return True
    else:
        return False
maxPalindrome=1
for numero1 in range(100,999):
    for numero2 in range(100,999):
        producto=numero1*numero2  
        if esPalindrom(producto):
            if producto>maxPalindrome:
                maxPalindrome=producto
                maxnum1=numero1
                maxnum2=numero2

print (maxPalindrome,maxnum1,maxnum2)

#Ejercicio_ 6 = Hacer una función que reciba una cedula como argumento y diga si la cedula es válida o no.


print("\t\t Ejercicio numero 6\n")


suma = 0
termino = False

cedula = int(input("Digite su número de cédula >>>"))
verificador = cedula

while (termino == False):

    while(verificador > 0):
        suma  = suma + (verificador %10)
        

    if (suma <= 11):
        termino = True
    else:
        verificador= suma
        suma  = 0

    print("El digito verificador es: " + str(suma))
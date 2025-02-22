# 1. Realiza las siguientes operaciones aritmeticas:
Suma = 15 + 25
Suma = (int(15 + 25))
print ('Resultado:',Suma)

Resta = 50 - 22
Resta = (int(50 - 22))
print ('Resultado:',Resta)

Multiplicacion= 8 * 7
Multiplicacion = (int(8 * 7))
print ('Resultado:',Multiplicacion)

Division= 100 / 20
Division = (int(100 / 20))
print ('Resultado:',Division)

# 2. Calcula el resto de la division de 37 entre 5 y almacenalo en una variable remainder. Luego imprmelo.
Division2 = 37 / 5
Division2 = (float(37 / 5))
remainder = (Division2)  
print (remainder)

# 3. Convierte el número 7 en una cadena de texto y concaténalo con la frase “ es mi número favorito”.Imprime el resultado
Numero = str(7)
print ("El", Numero,"es mi número favorito") 

# 4. Repite la palabra “Python” 10 veces usando el operador de multiplicación para cadenas y luego imprímela.
Python = "Python " * 10
print (Python)

# 5. Crea dos variables: a y b con los valores 12 y 8 respectivamente. Compara si a es mayor que b y almacena el resultado en una variable booleana resultado. Imprime el valor de resultado.
a = 12
b = 8

if a > b:
    resultado = True
print (resultado)

# 6. Compara dos cadenas de texto (“apple” y “banana”) usandolos operadores > y < y explica cuál tiene mayor orden alfabético.
apple = "apple"
banana = "banana"

if apple < banana:
    print ("apple")
else:
    print ("banana")
# Apple tiene mayor orden alfabético que banana porque la a es la primera letra del alfabeto   

# 7. Realiza una comparación lógica usando and para verificar si el número 10 es mayor que 5 y menor que 20. Imprime el resultado.
Numero = 10
if Numero > 5 and Numero < 20:
    print (True)

# 8. Usa el operador or para verificar si el numero 7 es menor que 3 o mayor que 5. Imprime el resultado.
Numero2 = 7
if Numero2 < 3 or Numero2 > 5:
    print (True)

# 9. Aplica el operador not para invertir el resultado de la comparacion 15 > 20. ¿Cual es el resultado?
Numero3 = 15
if not Numero3 > 20:
    print (True)

# 10. Combina operadores aritméticos y lógicos: Verifica si el número resultante de la expresión (5 * 3) + 2 es mayor que 10 y menor que 20. Imprime el resultado.
Op = (5 * 3) + 2
if Op > 10 and Op < 20:
    print (True)
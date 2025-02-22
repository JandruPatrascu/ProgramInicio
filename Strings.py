"Resolucion de Strings"
# Declara una variable text con la frase “Aprendiendo Python” y luego imprime la longitud de la cadena usando len()
text = "Aprendiendo Python"
print (len(text))

#Concatena dos cadenas: “Hola” y “Python”, y muestra el resultado en una sola línea.
Hola = "Hola"
Python = "Python"
print (Hola + Python)

#Crea una cadena que incluya un salto de línea, y luego imprímela para ver el resultado.
Sal = "Hola\nPython"
print (Sal)

#Usa el formateo de cadenas con f-strings para imprimir tu nombre, apellido y edad en una cadena de texto.
Nombre = "Alejandro"
Apellido = "Medina"
Edad = 21
print (f"Mi nombre es {Nombre} {Apellido} y tengo {Edad} años")

#. Desempaqueta los caracteres de la palabra “Python” en variables separadas y luego imprímelos uno por uno.
P = "P"
y = "y"
t = "t"
h = "h"
o = "o"
n = "n"
print (P), print (y), print (t), print (h), print (o), print (n)

#Extrae un “slice” de la palabra “Programación” para obtener los caracteres desde la posición 3 hasta la 7.
Progr = "Programación"
print (Progr[3:7])

#Invierte la cadena “Python” usando slicing y muestra el resultado
Python = "Python"
print (Python[::-1]) 

#. Convierte la cadena “aprendiendo python” en mayúsculas usando el método adecuado e imprímela.
Learn = "aprendiendo python"
print (Learn.upper())

#Cuenta cuántas veces aparece la letra “n” en la cadena “Programación en Python”.
Prog = "Programación en Python"
print (Prog.count("n"))

#Verifica si la cadena “12345” es numérica usando el método adecuado e imprime el resultado.
Num = "12345"
print (Num.isnumeric())
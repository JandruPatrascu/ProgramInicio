"Resolucion de Tuplas"

#1.Crea una tupla con los valores (10, 20, 30, 40, 50) e imprímela.
tupla = (10, 20, 30, 40, 50)
print(tupla)

#2.Accede al segundo elemento de la tupla (100, 200, 300,400, 500) y muéstralo.
tupla2 = (100, 200, 300, 400, 500)
print(tupla[1])

"""
#3.Intenta modificar el primer elemento de la tupla (1, 2,3) a 10 y observa el resultado.
tuple = (1, 2, 3)
tuple[0] = 10
print(tuple) #esto genera un error porque las tuplas no se pueden modificar
"""

#4.Cuenta cuántas veces aparece el número 3 en la tupla (1,2, 3, 3, 4, 5, 3).
my_tupla = (1, 2, 3, 3, 4, 5, 3)
print(my_tupla.count(3)) #el numero 3 aparece 3 veces en la tupla

#5.Encuentra el índice de la primera aparición de la cadena "Python" en la tupla ("Java", "Python", "JavaScript","Python").
my_tupla2 = ("Java", "Python", "JavaScript", "Python")
print(my_tupla2.index("Python")) #Error porque no se encuentra la cadena

#6.Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime la tupla resultante.
tup3 = (1, 2, 3) 
tup4 = (4, 5, 6)
tupla3 = tup3 + tup4 
print(tupla3)

#7.Crea una subtupla con los elementos desde la posición 2 hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30,40, 50).
tupla4 = (10, 20, 30, 40, 50)
subtupla = tupla4[2:4]
print(subtupla)

#8.Convierte la tupla ("rojo", "verde", "azul") en una lista, cambia el segundo elemento a "amarillo" y vuelve a convertirla en una tupla. Imprime la tupla resultante.
tup5 = ("rojo", "verde", "azul")
lista = list(tup5)
print(lista)
lista[1] = "amarillo"
tupla5 = tuple(lista)
print(tupla5)

#9.Elimina una tupla llamada my_tuple usando del y luego intenta imprimirla para ver el resultado.
my_tuple = (1, 2, 3)
del my_tuple
print(my_tuple) #Error porque la tupla fue eliminada

#10.Crea una tupla con un solo elemento (el número 100) e imprímela. Asegúrate de usar la sintaxis correcta para crear una tupla con un solo elemento.
tup6 = (100,)
print(tup6)
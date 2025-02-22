#Resolucion de Listas

#Crea una lista con los números del 1 al 5 e imprímela.
Lista = [1,2,3,4,5]
print (Lista)

#Accede e imprime el tercer elemento de la lista [10, 20,30, 40, 50].
List = [10,20,30,40,50]
print (List[2])

#Agrega el número 6 al final de la lista [1, 2, 3, 4, 5] e imprímela.
Lista2 = [1,2,3,4,5]
print (Lista2)
#agregando el numero 6
Lista2.append(6)
print (Lista2)

#Elimina el primer valor 30 de la lista [10, 20, 30, 30,40, 50].
List2 = [10,20,30,30,40,50]
print (List2)
#eliminando el primer valor 30
List2.remove(30)
print (List2)

#Usa la función pop() para eliminar el último elemento de la lista [1, 2, 3, 4, 5] y almacénalo en una variable.Imprime la variable y la lista.
Lista3 = [1,2,3,4,5]
print (Lista3)
#eliminando el ultimo elemento
Ultimo = Lista3.pop()
print (Ultimo)
#imprimiendo la variable sin El ultimo elemento
print (Lista3)

#Invierte la lista [100, 200, 300, 400, 500] e imprímela.
List3 = [100,200,300,400,500]
print (List3)
#invirtiendo 
List3.reverse()
print (List3)

#Ordena la lista [3, 1, 4, 2, 5] en orden ascendente e imprímela.
List4 = [3,1,4,2,5]
print (List4)
#ordenando
List4.sort()
print (List4)

#Concatena las listas [1, 2, 3] y [4, 5, 6] y almacena el resultado en una nueva lista. Imprime la lista resultante.
Lista4 = [1,2,3]
Lista5 = [4,5,6]
#concatenando
Lista6 = Lista4 + Lista5
print (Lista6)

#Crea una sublista con los elementos de la lista [10, 20, 30, 40, 50] que van desde la posición 1 hasta la 3 (sin incluir la posición 3).
List5 = [10,20,30,40,50]
print (List5[1:3])

'''
Hacer un progarama que tenga una lista de 8 numeros
enteros y haga los siguiente:
- Recorrer la lista y mostrarla (en una funcion)
- Ordenarla y mostrarla
- Mostrar su longitud
- Buscar algun elemento (que el usuario pida por teclado)
'''

from types import NoneType


lista = [1, 2, 4, 7, 8, 4, 7, 9]
############################################
def mostrar_lista():
    for numero in lista:
        print(f"Contenido de la posicion {lista.index(numero) + 1}: {numero}")

mostrar_lista()

############################################
lista.sort()
print(f"Lista ordenada: {lista}")
############################################
print(f"Longitud de la lista {len(lista)}")
############################################
dato = NoneType
while not isinstance(dato, int) or dato < 0:
    dato = int(input("Indique el numero que desea buscar en la lista: "))

if dato in lista:
    print(f"El dato si se encuentra en la lista y esta en la posicion: {lista.index(dato)}")
else:
    print("El dato introducido no esta en la lista.")
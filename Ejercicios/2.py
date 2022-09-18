'''
Crear un script que tenga 4 variables, una lista, un
string, un entero, y un boolenao y que imprima un mensaje
segun el tipo de dato de cada variable
'''

lista = [1, 3, 2]
texto = "Hola"
numero = 10
bool = True

def comprobar_tipo(variable):
    return type(variable)

print(comprobar_tipo(lista))
print(comprobar_tipo(texto))
print(comprobar_tipo(numero))
print(comprobar_tipo(bool))
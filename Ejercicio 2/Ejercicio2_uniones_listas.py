"""
EJERCICIO 2 — Combinar Dos Listas
##################################

Escribí una función llamada `combinar_listas(lista1, lista2)` que reciba dos listas
como parámetros y devuelva una nueva lista con todos los elementos de ambas,
primero los de `lista1` y luego los de `lista2`.

Importante: no uses el operador `+` entre listas ni el método `.extend()`.
Debés recorrer cada lista con un bucle y construir la nueva lista elemento por elemento.

Luego llamá a la función con los siguientes ejemplos e imprimí los resultados:

    lista_a = [1, 2, 3]
    lista_b = [4, 5, 6]
    # Resultado esperado: [1, 2, 3, 4, 5, 6]

    lista_c = ["manzana", "pera"]
    lista_d = ["naranja", "uva", "durazno"]
    # Resultado esperado: ["manzana", "pera", "naranja", "uva", "durazno"]

"""
#version 1
lista1 =  [1, 2, 3]
lista2 =  [4, 5, 6]

lista_c = ["manzana", "pera"]
lista_d = ["naranja", "uva", "durazno"]

def combinar_listas(lista1, lista2):
    lista3= []
    for caracteres in (lista1):
        lista3.append(caracteres)
    for caracteres in (lista2):
            lista3.append(caracteres)
    return lista3
        
print(combinar_listas(lista_c, lista_d))

#version 2
def combinar_listas2(lista1, lista2):
    lista3= []
    for lista in (lista1, lista2):
        for caracter in lista:
            lista3.append(caracter)
    return lista3

print(combinar_listas2(lista1, lista2))


#forma no pedida en el ejercicio.
def combinar_listas3(lista1, lista2):
    return lista1 + lista2

print(combinar_listas3(lista1, lista2))



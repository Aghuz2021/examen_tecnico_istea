"""
EJERCICIO 3 — Eliminar Duplicados de una Lista
################################################

Escribí una función llamada `eliminar_duplicados(lista)` que reciba una lista
y devuelva una nueva lista con los mismos elementos pero sin repetidos.
El orden de aparición de los elementos debe mantenerse (se conserva la primera vez
que aparece cada elemento).

Importante: no uses `set()` para resolver esto.
Debés recorrer la lista con un bucle y verificar manualmente si el elemento ya fue agregado.

Luego llamá a la función con los siguientes ejemplos e imprimí los resultados:

    lista1 = [1, 2, 3, 1, 2, 4]
    # Resultado esperado: [1, 2, 3, 4]

    lista2 = ["Pedro", "Florencia", "Ana", "Pedro", "Ana"]
    # Resultado esperado: ["Pedro", "Florencia", "Ana"]

    lista3 = [1, 2, 3, 1, 2, 4, "Pedro", "Florencia", "Ana", "Pedro"]
    # Resultado esperado: [1, 2, 3, 4, "Pedro", "Florencia", "Ana"]

"""

def eliminar_duplicados(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

# Ejemplos de uso
lista1 = [1, 2, 3, 1, 2, 4]
print(eliminar_duplicados(lista1))  # Resultado esperado: [1, 2, 3, 4]

lista2 = ["Pedro", "Florencia", "Ana", "Pedro", "Ana"]
print(eliminar_duplicados(lista2))  # Resultado esperado: ["Pedro", "Florencia", "Ana"]

lista3 = [1, 2, 3, 1, 2, 4, "Pedro", "Florencia", "Ana", "Pedro"]
print(eliminar_duplicados(lista3))  # Resultado esperado: [1, 2, 3, 4, "Pedro", "Florencia", "Ana"]
# EJERCICIO 2 — Combinar Dos Listas

Escribí una función llamada `combinar_listas(lista1, lista2)` que reciba dos listas como parámetros y devuelva una nueva lista con todos los elementos de ambas, primero los de `lista1` y luego los de `lista2`.

**Importante:** no uses el operador `+` entre listas ni el método `.extend()`. Debés recorrer cada lista con un bucle y construir la nueva lista elemento por elemento.

### Ejemplos esperados:

```python
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
# Resultado esperado: [1, 2, 3, 4, 5, 6]

lista_c = ["manzana", "pera"]
lista_d = ["naranja", "uva", "durazno"]
# Resultado esperado: ["manzana", "pera", "naranja", "uva", "durazno"]
```

---

## Explicación de las Soluciones

A continuación se presentan tres enfoques distintos para resolver este problema, analizando cómo funciona cada uno.

### Versión 1: Bucles Secuenciales (El enfoque directo)

```python
def combinar_listas(lista1, lista2):
    lista3= []
    for caracteres in (lista1):
        lista3.append(caracteres)
    for caracteres in (lista2):
            lista3.append(caracteres)
    return lista3
```

**Explicación:**
Esta versión cumple al 100% con la consigna. Funciona creando una nueva lista vacía (`lista3`). Luego, utiliza un bucle `for` para recorrer uno por uno los elementos de la primera lista y los agrega al final de la nueva lista usando el método `.append()`. Una vez que termina, ejecuta un segundo bucle `for` idéntico para la segunda lista. Es una solución muy fácil de leer y de entender paso a paso.

---

### Versión 2: Bucles Anidados (El enfoque optimizado o DRY)

```python
def combinar_listas2(lista1, lista2):
    lista3= []
    for lista in (lista1, lista2):
        for caracter in lista:
            lista3.append(caracter)
    return lista3
```

**Explicación:**
Esta versión también cumple con todas las reglas del ejercicio, pero es un poco más elegante e inteligente. Para evitar escribir dos bucles `for` separados (lo que se conoce en programación como violar el principio *DRY: Don't Repeat Yourself* o "No te repitas"), agrupa las dos listas en una tupla `(lista1, lista2)`. 
El primer bucle itera sobre las listas (primero toma `lista1` y luego `lista2`), y el bucle interno recorre los elementos individuales de la lista que esté de turno para agregarlos a `lista3`. El resultado es el mismo, pero el código es más compacto.

---

### Versión 3: El enfoque "Pythónico" (Fuera de consigna)

```python
def combinar_listas3(lista1, lista2):
    return lista1 + lista2
```

**Explicación:**
Esta versión muestra cómo se resolvería este problema en un entorno de trabajo real. Utiliza el operador de concatenación `+`, el cual está optimizado internamente en Python para unir dos listas de manera inmediata y crear una nueva. Aunque **no está permitido según las reglas de este ejercicio específico** (porque el objetivo era practicar bucles), es la forma más limpia, rápida y "pythónica" de hacerlo en el día a día del desarrollo.
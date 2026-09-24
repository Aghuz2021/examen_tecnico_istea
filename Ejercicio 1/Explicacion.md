# EJERCICIO 1 — Validar Contraseña

Escribí una función llamada `validar_contrasena(contrasena)` que reciba un string y retorne `True` si la contraseña es válida, o `False` si no lo es.

### Condiciones que debe cumplir una contraseña válida:

1. Debe tener al menos 8 caracteres.
2. Debe contener al menos una letra mayúscula (A-Z).
3. Debe contener al menos una letra minúscula (a-z).
4. Debe contener al menos un dígito (0-9).
5. No debe contener espacios en blanco.

> **Importante:** No uses expresiones regulares (módulo `re`). Recorré el string con un bucle y verificá cada condición manualmente.

### Ejemplos:

```python
validar_contrasena("Hola1234")      # True
validar_contrasena("hola1234")      # False  (sin mayúscula)
validar_contrasena("HOLA1234")      # False  (sin minúscula)
validar_contrasena("HolaMundo")     # False  (sin dígito)
validar_contrasena("Hola 123")      # False  (tiene espacio)
validar_contrasena("Ho1")           # False  (menos de 8 caracteres)
```

---
💡 **Ayuda:** podés usar los métodos `.isupper()`, `.islower()` y `.isdigit()` para verificar el tipo de cada carácter dentro del bucle.

# Explicación de Soluciones: Ejercicio 1 — Validar Contraseña

Este documento detalla las dos versiones desarrolladas para resolver el problema de validación de contraseñas. Ambas versiones cumplen con la restricción principal: no utilizar expresiones regulares (módulo `re`) y recorrer los strings manualmente mediante bucles. Sin embargo, cada una adopta un enfoque diferente en cuanto a su estructura y el tipo de respuesta.

---

## Versión 1 (`Ejercicio1_v1.py`) — Enfoque Lógico Booleano

Esta versión es estricta con la consigna original y se enfoca en retornar valores booleanos (`True` o `False`) comprobando las condiciones de manera simultánea.

### Características principales:
* **Alta Modularidad:** El problema se divide en 5 funciones auxiliares independientes, una para cada regla (`caracteres_mayor_ocho`, `tiene_mayuscula`, `tiene_minuscula`, `tiene_digito`, `no_tiene_espacios`).
* **Uso de métodos nativos:** Aprovecha métodos integrados de Python como `.isdigit()` para facilitar la verificación dentro de los bucles.
* **Comprobación con operador `and`:** La función principal `validar_contrasena` actúa como un orquestador. Ejecuta todas las funciones auxiliares y junta sus resultados usando el operador lógico `and`. 
* **Resultado:** Si todas las funciones retornan `True`, el resultado final es `True`. Si falla una sola condición, retorna `False`. Es un código muy claro y fácil de mantener.

---

## Versión 2 (`ejercicio1_v2.py`) — Enfoque Descriptivo con `Match-Case`

Esta versión mejora la experiencia del usuario (o del desarrollador que usa la función) proporcionando *feedback* exacto sobre qué regla no se cumplió, aprovechando características modernas de Python (versión 3.10 en adelante).

### Características principales:
* **Validaciones manuales puras:** A diferencia de la V1, aquí se comprueban los rangos de caracteres directamente usando comparaciones ASCII (por ejemplo, `"0" <= caracter <= "9"`) en lugar de depender de métodos como `.isdigit()`. Además, la validación de espacios es más estricta al incluir tabulaciones (`\t`) y saltos de línea (`\n`).
* **Estructura `match-case`:** Es el núcleo de esta versión. Utiliza la estructura `match` combinada con guardas (condicionales `if` dentro del `case`, como `case c if not tiene_mayuscula(c):`) para evaluar la contraseña secuencialmente.
* **Retorno de Mensajes (Strings):** En lugar de devolver un simple `False`, la función se detiene en el primer error que encuentra y devuelve un mensaje de texto descriptivo (ej. `"Error: Debe contener al menos una mayúscula (A-Z)."`). Si supera todas las condiciones, cae en el caso por defecto (`case _:`) y retorna `"¡Contraseña válida!"`.

### Conclusión de las versiones
Mientras que `Ejercicio1_v1.py` es ideal para la lógica interna de un programa donde solo importa saber si la contraseña pasó o no el filtro, `ejercicio1_v2.py` es excelente para interactuar con interfaces de usuario, donde se necesita explicar exactamente qué falta corregir.
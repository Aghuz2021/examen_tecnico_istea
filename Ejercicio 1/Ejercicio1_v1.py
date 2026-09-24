"""
EJERCICIO 1 — Validar Contraseña
##################################

Escribí una función llamada `validar_contrasena(contrasena)` que reciba un string
y retorne `True` si la contraseña es válida, o `False` si no lo es.

Condiciones que debe cumplir una contraseña válida:

1. Debe tener al menos 8 caracteres.
2. Debe contener al menos una letra mayúscula (A-Z).
3. Debe contener al menos una letra minúscula (a-z).
4. Debe contener al menos un dígito (0-9).
5. No debe contener espacios en blanco.

No uses expresiones regulares (módulo `re`). Recorré el string con un bucle
y verificá cada condición manualmente.

Ejemplos:

    validar_contrasena("Hola1234")      # True
    validar_contrasena("hola1234")      # False  (sin mayúscula)
    validar_contrasena("HOLA1234")      # False  (sin minúscula)
    validar_contrasena("HolaMundo")     # False  (sin dígito)
    validar_contrasena("Hola 123")      # False  (tiene espacio)
    validar_contrasena("Ho1")           # False  (menos de 8 caracteres)

Ayuda: podés usar los métodos `.isupper()`, `.islower()` y `.isdigit()` para
verificar el tipo de cada carácter dentro del bucle.

"""

contrasenia = "Hola 123"


def caracteres_mayor_ocho(contrasenia):
    if len(contrasenia) >= 8:
        return True
    return False


def tiene_mayuscula(contrasenia):
    for caracter in contrasenia:
        if "A" <= caracter <= "Z":
            return True
    return False


def tiene_minuscula(contrasenia):
    for caracter in contrasenia:
        if "a" <= caracter <= "z":
            return True
    return False


def tiene_digito(contrasenia):
    for caracter in contrasenia:
        if caracter.isdigit():
            return True
    return False


def no_tiene_espacios(contrasenia):
    for caracter in contrasenia:
        if caracter == " ":
            return False
    return True


def validar_contrasena(contrasenia):
    return (
        caracteres_mayor_ocho(contrasenia)
        and tiene_mayuscula(contrasenia)
        and tiene_minuscula(contrasenia)
        and tiene_digito(contrasenia)
        and no_tiene_espacios(contrasenia)
    )


print(validar_contrasena(contrasenia))
    
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
def tiene_mayuscula(contrasenia):
    for caracter in contrasenia:
        if "A" <= caracter <= "Z":  # Corregido: se evalúa 'caracter'
            return True
    return False


def tiene_minuscula(contrasenia):
    for caracter in contrasenia:
        if "a" <= caracter <= "z":  # Corregido: se evalúa 'caracter'
            return True
    return False  # Corregido: alineado fuera del bucle 'for'


def tiene_digito(texto):
    for caracter in texto:
        if "0" <= caracter <= "9":
            return True
    return False


def no_tiene_espacios(texto):
    for caracter in texto:
        if caracter in (" ", "\t", "\n"):
            return False
    return True


def validar_contrasena(clave):
    match clave:
        case c if len(c) < 8:
            return "Error: Debe tener al menos 8 caracteres."
        case c if not tiene_mayuscula(c):  # Corregido: agregado 'not'
            return "Error: Debe contener al menos una mayúscula (A-Z)."
        case c if not tiene_minuscula(c):  # Corregido: agregado 'not'
            return "Error: Debe contener al menos una minúscula (a-z)."
        case c if not tiene_digito(c):  # Corregido: agregado 'not'
            return "Error: Debe contener al menos un número (0-9)."
        case c if not no_tiene_espacios(c):  # Corregido: agregado 'not'
            return "Error: No debe contener espacios."
        case _:
            return "¡Contraseña válida!"
        

# Pruebas
print(validar_contrasena("Hola1234"))      # True
print(validar_contrasena("hola1234"))    # False  (sin mayúscula)
print(validar_contrasena("HOLA1234"))  # False  (sin minúscula)
print(validar_contrasena("HolaMundo"))     # False  (sin dígito)
print(validar_contrasena("Hola 123"))     # False  (tiene espacio)
print(validar_contrasena("Ho1"))          # False  (menos de 8 caracteres)
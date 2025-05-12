# 1. Función para saludar
# Recibe un nombre como parámetro y retorna un saludo personalizado.
def saludar(nombre):
    return f"¡Hola, {nombre}!"

# 2. Función para sumar dos números
# Retorna la suma de dos números recibidos como parámetros.
def sumar(a, b):
    return a + b

# 3. Función para calcular el área de un círculo
# Usa la fórmula área = pi * radio^2. Pi se define como 3.1416.
def area_circulo(radio):
    pi = 3.1416
    return pi * radio ** 2

# 4. Función para verificar si un número es par
# Retorna True si el número es par, False en caso contrario.
def es_par(numero):
    return numero % 2 == 0

# 5. Función para encontrar el mayor de tres números
# Utiliza la función max para obtener el valor más alto entre tres números.
def mayor_de_tres(a, b, c):
    return max(a, b, c)

# 6. Función para contar vocales en una cadena
# Convierte la cadena a minúsculas y cuenta cuántas vocales contiene.
def contar_vocales(cadena):
    cadena = cadena.lower()  # Ignora mayúsculas/minúsculas
    return sum(1 for c in cadena if c in 'aeiou')

# 7. Función para calcular el factorial (recursividad)
# Calcula el factorial de un número de forma recursiva.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 8. Función para verificar si una palabra es palíndromo
# Compara la palabra con su versión invertida para verificar si es igual.
def es_palindromo(palabra):
    palabra = palabra.lower()  # Ignora mayúsculas/minúsculas
    return palabra == palabra[::-1]

# 9. Función para generar la secuencia de Fibonacci
# Genera los primeros 'n' números de la secuencia de Fibonacci.
def fibonacci(n):
    secuencia = [0, 1]
    for i in range(2, n):
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia[:n]

# 10. Función para convertir Celsius a Fahrenheit
# Usa la fórmula: (C × 9/5) + 32
def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

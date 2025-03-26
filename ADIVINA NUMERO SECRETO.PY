"""Programa en el que tienes que adivinar un número aleatorio con pistas de si es mayor o menor al número introducido 
y consiguiendo más o menos puntos en función del número de intnetos"""

# Importación de librerías

import random  # Importamos la librería random para generar un número aleatorio

# Declaración de variables
intentos = 0  # Contador de intentos del jugador
intentos += 1  # Aumentamos el contador de intentos
numero_secreto = random.randint(1, 100)  # Generamos un número aleatorio entre 1 y 100
puntos = 50 # Número de puntos obtenidos
nombre = 0 # Nombre del jugador


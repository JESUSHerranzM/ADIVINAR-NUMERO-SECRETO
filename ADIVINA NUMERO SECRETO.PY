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

# Programa principal

def guardar_puntuacion(nombre, puntos):  # Define una función que recibe un nombre y una puntuación
    """Guarda la puntuación en un archivo de texto."""  
    with open("puntuaciones.txt", "a") as archivo:  # Abre el archivo en modo "append" (agregar al final del archivo sin borrarlo)
        archivo.write(f"{nombre}: {puntos} puntos\n")  # Escribe la puntuación en el archivo

def adivina_el_numero():  
    numero_secreto = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    intentos = 0  # Inicia el contador de intentos
    
    nombre = input("Introduce tu nombre: ")  # Pide el nombre del jugador
    print(f"Bienvenido {nombre} a: ¡Adivina el número!")  # Mensaje de bienvenida
    print("Estoy pensando en un número entre 1 y 100.")  # Indicación del juego

    while True:
        intento = int(input("Intenta adivinar el número: "))  # Pedimos al usuario un número
        intentos += 1  # Aumentamos el contador de intentos
        
        if intento < numero_secreto:
            print("El número es mayor SO PENCO. Inténtalo de nuevo CENUTRIO.")  # Indicamos que el número es mayor
        elif intento > numero_secreto:
            print("El número es menor CARA CULO. Inténtalo de nuevo INVÁLIDO.")  # Indicamos que el número es menor
        else:
            # Asignamos puntos según el número de intentos
            if intentos == 1:
                puntos = 50
            elif intentos <= 10:
                puntos = 50 - (intentos - 1) * 5  # Se reducen 5 puntos por intento extra
            else:
                puntos = 1  # Si tarda más de 10 intentos, solo obtiene 1 punto
            
            print(f"¡BIEN HECHO {nombre}! Adivinaste el número en {intentos} intentos y obtuviste {puntos} puntos.")  # Mensaje de éxito

adivina_el_numero()  # Llamamos a la función para iniciar el juego (prueba)     
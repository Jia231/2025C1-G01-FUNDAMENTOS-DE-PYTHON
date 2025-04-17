""" 
Autor: Jia Ming Liou
Fecha: 16-4-2025 
"""

import os
from modulo import ingresar_ventas, guardar_ventas, analizar_ventas
 
def limpiar_pantalla():
    """Limpia la pantalla de la terminal en ejecución"""
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("Digite Enter para seguir...")

def menu():
    ventas = []  
    pausar()
    while True:
        print("-----Menu principal-----")
        print("1. Ingresar ventas de cursos UMCA")
        print("2. Guardar datos en CSV")
        print("3. Analizar ventas")
        print("4. Salir")
        opcion = int(input("Seleccione una opcion: "))  

        if opcion == 4:
            break  
        elif opcion == 1:
            print("Ingresar cursos")
            pausar()
            ingresar_ventas(ventas)
            limpiar_pantalla()
        elif opcion == 2:
            print("Guardar archivo")
            guardar_ventas(ventas)
            pausar()
        elif opcion == 3:
            limpiar_pantalla()
            analizar_ventas()
            pausar()
        else:
            print("Intente nuevamente")
            pausar()                           

if __name__ == "__main__":
    print("Bienvenido al sistema de gestion de ventas")

menu()    





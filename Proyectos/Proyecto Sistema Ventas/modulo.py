import csv
import os
import pandas

def ingresar_ventas(lista_ventas):
    while True:
        try:
            curso = input("Ingrese el nombre del curso: ").upper()
            cantidad = int(input("Ingrese la cantidad de cursos vendidos: "))
            fecha = input("Ingrese la fecha de la venta (AAAA-MM-DD): ")
            precio = float(input("Ingrese el precio: "))
            cliente = input("Digite el nombre del cliente: ")
        except:
            print("Ingrese un valor valido")
            continue

        venta = {
            'curso': curso,
            'cantidad': cantidad,
            'fecha': fecha,
            'precio': precio,
            'cliente': cliente
        }

        lista_ventas.append(venta)

        continuar = input("Desear seguir? S/N").lower()
        if continuar == 's':
            continue
        elif continuar == "n":
            return lista_ventas
        else:
            print("Opcion no valida")


def guardar_ventas(ventas):

    if not ventas:
        print("No hay ventas")
    else: 
        if os.path.exists('ventas.csv'):
            with open('ventas.csv', 'a', newline='', encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo, fieldnames=["curso", "cantidad", "fecha", "precio", "cliente"])
                guardar.writerows(ventas)
        else:    
            with open('ventas.csv', 'w', newline='', encoding='utf-8') as archivo:
                guardar = csv.DictWriter(archivo, fieldnames=["curso", "cantidad", "fecha", "precio", "cliente"])
                guardar.writeheader()
                guardar.writerows(ventas)        
        print("Datos guardados exitosamente")


def analizar_ventas():
    df = pandas.read_csv("ventas.csv")
    print("------------Resumen de ventas-------------")
    df['subtotal'] = df['cantidad'] * df['precio']
    total_ingresos = df['subtotal'].sum()
    print(f"Total de ventas: {total_ingresos}")
    curso_mas_vendido = df.groupby('curso')['cantidad'].sum().idxmax()
    print(f'El curso mas vendido es {curso_mas_vendido}')
    cliente_mas_compras = df.groupby('cliente')['cantidad'].count().idxmax()
    print(f'El cliente com mas compras es  {cliente_mas_compras}')
    # result_df = df.groupby('Category').apply(lambda group: (group['Values1'] * group['Values2']).sum()).reset_index(name='Result')

    ventas_por_fecha = df.groupby('fecha')['subtotal'].sum()
    print("-----------Las ventas por fecha--------")
    print(ventas_por_fecha)
    
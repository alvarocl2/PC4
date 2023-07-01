#Se importan las librerías 'request', 'csv' y 'os'
import requests
import csv
import os
#Se solicita al usuario la cantidad de Bitcoins que tiene
while True:
    try:
        cantidad_Bitcoins=float(input("Ingrese la cantidad de Bitcoins con los que cuenta: "))
        break
    except ValueError:
        print('Dato inválido, inserte un número')
#Se obtiene el precio actual del Bitcoin desde la API
try:
    response=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response.raise_for_status()
    data=response.json()
    precio=data['bpi']['USD']['rate_float']
except (requests.RequestException, KeyError, ValueError):
    print("Error al obtener el precio de la Bitcoin.")
    exit()
#Se calcula el costo de los Bitcoins en USD
costo_Bitcoins = cantidad_Bitcoins * precio
#Se muestra el costo actual de las Bitcoins
print(f"El costo actual de {cantidad_Bitcoins} Bitcoins es: ${costo_Bitcoins:,.4f}")
#Se guarda el precio en un archivo de texto
with open('precio_bitcoin.txt', 'w') as file:
    file.write(str(precio))
#Se guarda el precio en un archivo CSV
csv_data = [['Cantidad de Bitcoins', 'Precio en USD', 'Costo Total en USD'],
            [cantidad_Bitcoins, precio, costo_Bitcoins]]
csv_file = 'precio_bitcoin.csv'
if not os.path.exists(csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)
else:
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)
#Se guarda el precio en un archivo de texto
with open('precio_bitcoin.txt', 'w') as file:
    file.write(str(precio))
# Se guarda el precio en un archivo CSV
csv_data = [['Cantidad de Bitcoins', 'Precio en USD', 'Costo Total en USD'],
            [cantidad_Bitcoins, precio, costo_Bitcoins]]
csv_file = 'precio_bitcoin.csv'
if not os.path.exists(csv_file):
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)
else:
    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)
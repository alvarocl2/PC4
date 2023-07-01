#Se importa la librería 'requests'
import requests
while True:
    try:
        #Se solicita al usuario la cantidad de Bitcoins que tiene
        cantidad_Bitcoins = float(input("Ingrese la cantidad de Bitcoins con los que cuenta: "))
        break
    except ValueError:
        #Si el dato ingresado es un str, devuelve "Dato inválido, intentelo de nuevo"
        print('Dato inválido, inserte un número')
#Se obtiene el precio actual del Bitcoin desde la API de CoinDesk
try:
    response=requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response.raise_for_status()
    data=response.json()
    precio= data['bpi']['USD']['rate_float']
#Si presenta un error, muestra "Error al obtener el precio de la Bitcoin"
except (requests.RequestException, KeyError, ValueError):
    print("Error al obtener el precio de la Bitcoin.")
    exit()
#Se calcula el costo de cada Bitcoin que tiene el usuario en USD
costo_Bitcoins=cantidad_Bitcoins* precio
#Mediante el print se muestra el costo actual de las Bitcoins (en USD con cuatro decimales y separador de miles)
print(f"El costo actual de {cantidad_Bitcoins} Bitcoins es: ${costo_Bitcoins:,.4f}")
#Se importa la librería 'requests'
import requests
#Se asigna el URL a una variable
url="https://images.unsplash.com/photo-1234567890"
response=requests.get(url)
#Verificar si la solicitud fue exitosa
if response.status_code==200:
    # Obtener el contenido de la respuesta (los datos de la imagen)
    imagen=response.content
    # Guardar la imagen en un archivo local
    with open("imagen.jpg", "wb") as file:
        file.write(imagen)
else:
    print("Error al descargar la imagen")
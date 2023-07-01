#Se importa la librería 'random' y 'figlet'
import random
from pyfiglet import Figlet
#Se obtiene la lista de las fuentes disponibles
figlet=Figlet()
lista_fuentes=figlet.getFonts()
#Se solicita al usuario el nombre de la fuente
seleccion_fuente=input("Ingrese el nombre de la fuente, de no elegirse, se elegirá una fuente random: ")
#Se selecciona una fuente aleatoria si no se ingresa ninguna fuente
if not seleccion_fuente:
    seleccion_fuente=random.choice(lista_fuentes)
elif seleccion_fuente not in lista_fuentes:
    print("La fuente ingresada no es válida, las fuentes válidas son: ")
    print(", ".join(lista_fuentes))
    exit()
#Se solicita al usuario el texto que debe imprimir
texto_a_imprimir=input("Ingrese el texto: ")
#Se configura la fuente seleccionada
figlet.setFont(font=seleccion_fuente)
#Se imprime el texto ingresado
print(figlet.renderText(texto_a_imprimir))
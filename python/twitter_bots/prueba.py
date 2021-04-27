import os
import random

#Genero el insulto

insulto = ("daltonica", "anorexica", "mal parida", "lamecalvas", "autista", "manca", "desenfocado")
sustantivo = ("puta", "foca", "mamarracha", "morsa", "orca", "araña", "semaforo", "zorra", "elefante", "retrovisor")
insultofinal = ("Malu"+" "+random.choice(sustantivo)+" "+random.choice(insulto))


#Abro el objeto texto y lo escribo
archivo = open('insulto.txt', 'w')
archivo.write(insultofinal)
archivo = open('insulto.txt', 'r')

#Resultado
print(archivo.read())

archivo.close()
os.remove("insulto.txt")
import tweepy
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

#Authenticate to Twitter
auth = tweepy.OAuthHandler("oLaFN2Ycx8Q7bzgf9F3QC3Vj2", "90VjX7iaIEjYqDbAovL2kKrRzaQxhQiZImw5H2nJEo9JoHJhHZ")
auth.set_access_token("735885736776437760-r09rgpFT8eqGj35lKJKjMpd5Ikmha55", "nY68hEOg4TDD0Ksny8q6j2CYjK2p2yeZ0YhIBPX5ZpxNY")

#Creando objeto API
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

#Creando un tweet
api.update_status(archivo.read())

#Cierra el enlace con el archivo
archivo.close()

#Limpia los archivos residuales
os.remove("insulto.txt")
import pygame

pygame.mixer.init()
cancion=str(input("Seleccione una cancion: "))
pygame.mixer.music.load(cancion)
pygame.mixer.music.set_volume(0.7)
pygame.mixer.music.play()

while True:
	print("Pulsa p para pausar la cancion")
	print("Pulsa r para reanudar la cancion")
	print("Pulsa e para elegir una cancion")
	print("Pulsa s para salir")

	opcion=input(">>> ")

	if opcion=="p":
		pygame.mixer.music.pause()
	elif opcion=="r":
		pygame.mixer.music.unpause()
	elif opcion=="s":
		pygame.mixer.music.stop()
	elif opcion=="e":
		pygame.mixer.music.stop()
		cancion=str(input("Seleccione una cancion: "))
		pygame.mixer.music.load(cancion)
		pygame.mixer.music.set_volume(0.7)
		pygame.mixer.music.play()

	else:
		break
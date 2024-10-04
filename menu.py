from Laberinto import run_laberinto,run_laberinto_grande

def menu():
	print("*** MENU ***")
	print("1.-Laberinto chico")
	print("2.-Laberinto grande")
	print("3.-Salir")
	while True:
		opcion = int(input("Ingresa la opción deseada entre 1-3:"))
		if opcion >= 1 and opcion <=3:
			break
		else:
			print("Valor incorrecto")
	return opcion

if __name__ == "__main__": 
	while True:
		opcion = menu()
		if opcion == 1:
			run_laberinto()
		elif opcion == 2:
			run_laberinto_grande()
		else:
			print("Gracias por utilizar busqueda informada Lab4")
			exit(0)
from Puzzle import run_puzzle
from Laberinto import run_laberinto



def menu():
	print("*** MENU ***")
	print("1.-Puzzle")
	print("2.-Laberinto")
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
			run_puzzle()
		elif opcion == 2:
			run_laberinto()
		else:
			print("Gracias por utilizar busqueda no informada P1")
			exit(0)
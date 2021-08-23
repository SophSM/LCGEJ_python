# Working with files
nombre = input("Ingrese nombre del archivo: ")
file = open(nombre, 'r')
linea = 0
lista = []
file2 = open('nuevo_archivo.txt', 'w')
for line in file:
	linea += 1
	if ((linea % 2) == 0):
		file2.write(line)

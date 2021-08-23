# Dictionaries
s = input("Ingrese string: ")
diccionario = {}
for palabra in s.split(' '):
	diccionario[palabra] = 0
for palabra in s.split(' '):
	diccionario[palabra] += 1
for key, value in diccionario.items():
	print(key, ' ', value)

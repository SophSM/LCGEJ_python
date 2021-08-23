# Conditions and Loops
a = int(input("Dame a: "))
b = int(input("Dabe b: "))
if (a < b) and (b < 10000):
	numeros = list(range(a, b + 1))
	suma = 0
	rango = len(numeros)
	for i in range(rango):
		if ((numeros[i] % 2) == 1):
			suma += numeros[i]
	print(suma)

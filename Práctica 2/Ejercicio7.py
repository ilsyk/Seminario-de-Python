import string
from collections import Counter

cadena = input("Ingrese cadena o frase: ")

"""letras = set(string.ascii_letters)
print(letras)
"""
apariciones = Counter(cadena.lower()).most_common()
# apariciones = lista de tuplas con cada letra y cantidad de veces que aparece
# dicha letra en la cadena o frase
print(apariciones)
apariciones2 = Counter("a")
for i in apariciones:
	if i[0] in string.ascii_lowercase and i[1] > 1:
		print("Esta cadena o frase no es un holograma")
		break;
from collections import Counter

cadena = input("Ingrese una palabra o frase: ")
apariciones = Counter(cadena.lower()).most_common()

if apariciones[0][1] > 1:
	print(f"'{cadena}' no es un holograma")
else:
	print(f"'{cadena}' es un holograma")
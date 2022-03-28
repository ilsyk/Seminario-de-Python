# Ingresar palabras desde el teclado hasta ingresar la palabra FIN. Imprimir
# aquellas que empiecen y terminen con la misma letra.

palabra = input("Ingresar palabra: ")

while palabra != "fin":
	# comparo letra inicial con letra final, uso la función lower
	# por si hay letras mayúsculas y minúsculas
	if palabra[0].lower() == palabra[-1].lower():
		print(palabra)
	palabra = input("Ingresar palabra: ")
from time import sleep

# Abro todos los archivos correspondientes y los convierto en listas
with open("nombres_1.txt", mode="r", encoding="utf8") as nombres1:
	nombres1 = nombres1.read().lower().replace(",", "").replace("'", "").split()
with open("nombres_2.txt", mode="r", encoding="utf8") as nombres2:
	nombres2 = nombres2.read().lower().replace(",", "").replace("'", "").split()
with open("eval1.txt", mode="r") as eval1:
	eval1 = eval1.read().replace(",", "").split()
with open("eval2.txt", mode="r") as eval2:
	eval2 = eval2.read().replace(",", "").split()


def nombres_en_ambos(lista1, lista2):
	"""
	Parámetros: nombres_1, nombres_2
	Función que imprime los nombres que se encuentran en ambos archivos de texto.
	"""

	# Genero una conjunto con los nombres que aparacecen en ambas listas
	ambos = set([nombre for nombre in lista1 if nombre in lista2])

	# Imprimo conjunto
	for nombre in ambos:
		print(f"{nombre.title()} aparece en ambos.")

def imprimir (names, eval1, eval2):
	"""
	Párametros:  archivos de texto nombres_1, eval1 y eval2
	Función que imprime los nombres, ambas notas y suma de ambas notas
	de los archivos de texto.
	"""
	print(f"   {'Nombre':10} {'Eval1':10}{'Eval2':10}{'Total':14}")
	i = 0
	# Voy recorriendo los tres archivos en relación 1:1 e imprimiendo 
	for nom, nota1, nota2 in zip(names, eval1, eval2):
		total = int(nota1) + int(nota2)
		sleep(0.5)
		print(f"{i:>2} {nom.title():<12}{nota1:<10}{nota2:<10}{total:<10}")
		i += 1


nombres_en_ambos(nombres1, nombres2)
print("--------------------------------------------------")
imprimir(nombres1, eval1, eval2)
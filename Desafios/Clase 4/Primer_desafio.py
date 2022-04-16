import csv


def titulos_veinte_veintiuno():
	"""
	Función que recorre archivo csv de titulos de netflix y crea nueva lista
	con los titulos de 2021. 
	Devuelve dicha lista.
	"""
	archivo = open("netflix_titles.csv", mode="r", encoding="utf8")
	reader = csv.reader(archivo, delimiter=",")

	veinte_veintiuno = list(filter(lambda titulo: titulo[7] == "2021", reader))

	archivo.close()

	return veinte_veintiuno

def crear_nuevo_archivo(titulos):
	"""
	Parámetros: lista con los titulos de netflix de 2021
	Función que guarda en un archivo los titulos de la lista 
	"""
	with open("titulos_2021.csv", mode="w", encoding="utf8", newline="") as nuevo_archivo:
		writer = csv.writer(nuevo_archivo, delimiter=",")
		writer.writerows(titulos)


lista_titulos = titulos_veinte_veintiuno()
crear_nuevo_archivo(lista_titulos)
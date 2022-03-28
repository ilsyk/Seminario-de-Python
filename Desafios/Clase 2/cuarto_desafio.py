"""Necesitamos procesar las notas de los estudiantes de este curso.
Queremos saber:
 cuál es el promedio de las notas,
 qué estudiantes están por debajo del promedio
"""
def ingreso_notas():
	# Esta función retorna un diccionario con los nombres y notas de los estudiantes.
	nombre = input("Ingresa un nombre (<FIN> para finalizar): ")
	dicci = {}
	while nombre != "FIN":
		nota = int(input(f"Ingresa la nota de {nombre}: "))
		dicci[nombre] = nota
		nombre = input("Ingresa un nombre (<FIN> para finalizar): ")
	return dicci

def calculo_promedio(notas):
	# función que retorna promedio de notas de los estudiantes
	total_notas = 0
	# recorro valores del diccionario (notas), para calcular total notas
	for nota in notas.values():
		total_notas += nota
	promedio = total_notas / len(notas)
	return promedio

def calcular_cantidad (promedio, estudiantes):
	# función que retorna cuántos estudiantes tienen notas menores al promedio
	cant = 0
	for nota in estudiantes.values():
		if nota < promedio:
			cant += 1
	return cant

notas_de_estudiantes = ingreso_notas()
print(notas_de_estudiantes)
promedio_notas = calculo_promedio(notas_de_estudiantes)
print(f"Promedio de las notas {promedio_notas}")
cantidad = calcular_cantidad(promedio_notas, notas_de_estudiantes)
print(f"Cantidad de alumnos con notas menores al promedio: {cantidad}")
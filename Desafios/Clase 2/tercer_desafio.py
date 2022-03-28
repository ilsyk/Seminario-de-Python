# Ingresar las notas
# Calcular el promedio
# Calcular cuántos tienen notas menores al promedio

nota = int(input("Ingresá una nota (-1 para finalizar): "))
lista_de_notas = []
# inicializo contadores de notas para luego calcular promedio
total_notas = 0
cant_alumnos = 0
while nota != -1:
	lista_de_notas.append(nota)
	total_notas += nota
	cant_alumnos += 1
	nota = int(input("Ingresá una nota (-1 para finalizar): "))
# calculo promedio de notas
promedio = total_notas / cant_alumnos 
print(f"Promedio de las notas: {promedio}")
# cuento cantidad de alumnos con nota menor al promedio
cant_alumnos_menor = 0
for nota in lista_de_notas:
	if nota < promedio:
		cant_alumnos_menor += 1
print(f"Cantidad de alumnos con nota menor al promedio {cant_alumnos_menor}")

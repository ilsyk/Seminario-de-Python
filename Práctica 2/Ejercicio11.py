with open("nombres_1.txt", mode="r", encoding="utf8") as nombres1:
	nombres1 = nombres1.read().lower().replace(",", "").replace("'", "").split()
with open("nombres_2.txt", mode="r", encoding="utf8") as nombres2:
	nombres2 = nombres2.read().lower().replace(",", "").replace("'", "").split()
with open("eval1.txt", mode="r") as eval1:
	eval1 = eval1.read().replace(",", "").split()
with open("eval2.txt", mode="r") as eval2:
	eval2 = eval2.read().replace(",", "").split()

ambos = set([nombre for nombre in nombres1 for nombre2 in nombres2 if nombre == nombre2])

for nombre in ambos:
	print(f"{nombre} aparece en ambos.")

def imprimir (names, eval1, eval2):
	i = 0
	print(f"   {'Nombre':10} {'Eval1':10}{'Eval2':10}{'Total':14}")
	for nom, nota1, nota2 in zip(names, eval1, eval2):
		total = int(nota1) + int(nota2)
		print("{:>2} {:<12}{:<10}{:<10}{:<10}".format(i, nom.title(), nota1, nota2, total))
		i += 1

imprimir(nombres1, eval1, eval2)
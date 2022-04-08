with open("README.md", mode="r") as file:
	texto = file.read().split("\n")
# genero lista con todas las lineas que tengan "http" o "https"
links = filter(lambda linea: "http" in linea or "https" in linea, texto)

for i in links:
	print(i)

file.close()
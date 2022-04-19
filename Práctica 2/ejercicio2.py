from collections import Counter

with open("README.md", mode="r") as file:
	texto = file.read().replace("-", "").replace(",", "")

c = Counter(texto.lower().split())
# retorna la palabra con más apariciones
print(c.most_common(1))
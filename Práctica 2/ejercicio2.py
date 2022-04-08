from collections import Counter

with open("README.md", mode="r") as file:
	texto = file.read().replace("-", "").replace(",", "")

c = Counter(texto.lower().split())
# most_common(n) retorna las n palabras con más apariciones
print(c.most_common(1))
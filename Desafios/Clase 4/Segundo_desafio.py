from collections import Counter
import csv

archivo = open("titulos_2021.csv", mode="r", encoding="utf8")
reader = csv.reader(archivo, delimiter=",")

paises = list(map(lambda pais: pais[5], reader))
print(Counter(paises).most_common(6))
archivo.close()
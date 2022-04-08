frase = "Una frase para testear el code".lower()

string = input("Ingrese string: ").lower()

cantidad = frase.lower().count(string)
print(f"Cantidad de veces que aparece {string} en la frase: {cantidad}")
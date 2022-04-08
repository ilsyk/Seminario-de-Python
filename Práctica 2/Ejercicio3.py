import string

text = "Este texto es para testear el correcto funcionamiento del programa"
# solicito letra por teclado y verifico que sea una letra
letter = input("Ingrese una letra: ")
if letter not in string.ascii_letters:
	print(f"ERROR.")
else:
	for word in text.lower().split():
		if letter.lower() in word[0]:
			print(word)
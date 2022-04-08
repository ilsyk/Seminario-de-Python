cadena = input("""Ingresa la clave (debe tener menos de 10 caracteres y no
contener los símbolos:@ y !): """)
if len(cadena) > 10:
	print("Ingresaste más de 10 caracteres")
elif cadena.count("@") != 0 or cadena.count("!") != 0:
	print("Se ingreso un caracter no valido")
else:
	print('cadena valida')
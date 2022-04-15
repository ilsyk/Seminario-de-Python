celdas = [
'-*-*-',
'--*--',
'----*',
'*----',
]


def generar_numerica(celdas):
    """
    Parámetros: estructura de celdas inicial
    Genero celdas numericas a partir de la estructura inicial
    """
    nueva = []   # nueva estructura
    for linea in celdas:
        nueva_linea = [0 if elem == "-" else -1 for elem in linea] 
        nueva.append(nueva_linea)
    return nueva

def actualizar_horizontal(linea, pos):
    """
    Parámetros: linea y posicion
    Funcion que actualiza los vecinos de la celda en la posicion dada
    """
    if pos == 0:
        linea[pos+1] += 1
    elif pos == 1 or pos == 2 or pos == 3:
        linea[pos+1] += 1
        linea[pos-1] += 1
    elif pos == 4:
        linea[pos-1] += 1
    return linea

def actualizar_vertical(celdas, linea, pos):
    """
    Función que actualiza arriba y abajo en la posicion donde hay bombas
    """
    if linea == 0:
        celdas[linea+1][pos] += 1
    elif linea == 1 or linea == 2:
        celdas[linea+1][pos] += 1
        celdas[linea-1][pos] += 1
    elif linea == 3:
        celdas[linea-1][pos] += 1
    return celdas

def actualizar_alrededor(celdas):
    """
    Parámetro: celda numerica
    Función que actualiza las celdas que tienen bomba a su alrededor
    """
    for linea in range(len(celdas)):    # por cada linea
        for elem in range(len(celdas[linea])):  # por cada elemento en la linea
            if celdas[linea][elem] == -1:
                celdas[linea][elem] = "*"
                # Paso linea a actualizar y posicion del elemento
                celdas[linea] = actualizar_horizontal(celdas[linea], elem)
                # Paso estructura completa, posicion de linea y de elemento
                celdas = actualizar_vertical(celdas, linea, elem)
    return celdas

def convertir_string(celdas):
    """
    Parámetros: nueva_celda 
    Función que convierte la celda numérica ya actualizada al formato string
    de la estructura original.
    """
    convertida = []
    for linea in range(len(celdas)):    # por cada linea
        for elem in range(len(celdas[linea])):  # por cada elemento en la linea
            # Convierto todos los elementos a string
            celdas[linea][elem] = str(celdas[linea][elem])
        # Cada linea, que es una lista, la convierto a string 
        celdas[linea] = "".join(celdas[linea])
    return celdas


nueva_celda = generar_numerica(celdas)
nueva_celda = actualizar_alrededor(nueva_celda)
nueva_celda = convertir_string(nueva_celda)
for linea in celdas:
    print(linea)
print()
for linea in nueva_celda:
    print(linea)
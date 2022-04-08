import string

evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.
"""

# inicializo contadores
facil = 0
aceptable = 0
dificil = 0
muy_dificil = 0

# saco "resumen:" del texto
texto = evaluar.split("resumen:")

# lista con las oraciones
oraciones_resumen = texto[1].split(".")
# saco la cantidad de palabras de cada oracion
for oracion in oraciones_resumen:
	palabras = oracion.split()
	cont = 0
	for i in palabras:
		cont += 1
	if cont <= 12:
		facil += 1
	elif cont <= 17:
		aceptable += 1
	elif cont <= 25:
		dificil += 1
	else:
		muy_dificil += 1

print(f"Cantidad de oraciones fáciles de leer: {facil}, aceptables para leer:{aceptable}, dificil de leer: {dificil}, muy dificil de leer: {muy_dificil}")
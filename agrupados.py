# Desafío - Ventas
# Patricio Cortés
# G18
# 20-09-2021

# importa libreria itertools
from itertools import groupby

# define un diccionario con nombre ventas
ventas = [20000, 30000, 40000, 20000, 40000, 20000, 20000, 30000, 30000, 20000, 40000, 20000]

# ordena los valores 
ventas.sort()

# define diccionario "dic"
dic = {k: len(list(v)) for k, v in groupby(ventas)}

# imprime el resulatado de la funcion
print(dic)

# Fin de Programa
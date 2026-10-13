# inspeccion.py — Tipos, columna derivada e indicadores (Python)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   python scripts/inspeccion.py

# TODO 1: carga data/ventas.csv
# TODO 2: imprime los tipos (dtypes) de cada columna
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total


import pandas as pd

ventas = pd.read_csv("data/ventas.csv")
ventas["ticket"] = ventas["ventas"]/ventas["clientes"] ##nueva columna
print(ventas.head())

##imprimir el maximo en ventas
print("\n")
#print(ventas["ventas"].max())

##localizar indice o tupla asociado a un identificador, en este caso, la 
##sucursal con mayor ventas 
print("Sucursal con mayor ventas", ventas.loc[ventas["ventas"].idxmax(), "sucursal"])

##imprimir la sucursal con menor ventas
print("Sucursal con menor ventas", ventas.loc[ventas["ventas"].idxmin(), "sucursal"])
print("\n")

ventas_per_region = ventas.groupby("region").sum("ventas")
ventas_per_region.head()

##tarea: sacar la maxima de las regiones


# inspeccion.R — Tipos, columna derivada e indicadores (R)
# Completa los pasos marcados con TODO. Ejecuta desde la raíz del repositorio:
#   Rscript scripts/inspeccion.R

# TODO 1: carga data/ventas.csv
# TODO 2: imprime la estructura (str) para ver los tipos
#         (fija si region llegó como character o factor)
# TODO 3: crea la columna derivada "ticket" = ventas / clientes
# TODO 4: calcula e imprime:
#         - venta promedio por sucursal (aggregate o dplyr)
#         - ticket promedio (ventas totales / clientes totales)
#         - sucursal con mayor y menor venta
#         - región con mayor venta total

ventas <- read.csv("data/ventas.csv")

str(ventas)

ventas$ticket <- ventas$ventas / ventas$clientes
head(ventas)

aggregate(ventas ~ sucursal, data = ventas, mean)

sum(ventas$ventas) / sum(ventas$clientes)

ventas$sucursal[which.max(ventas$ventas)]
ventas$sucursal[which.min(ventas$ventas)]

regiones <- aggregate(ventas ~ region, data = ventas, sum)
regiones$region[which.max(regiones$ventas)]

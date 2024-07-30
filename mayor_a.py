import sys

#Diccionario de ventas proporcionado
ventas = {
    "Enero" : 15000,
    "Febrero" : 22000,
    "Marzo" : 12000,
    "Abril" : 17000,
    "Mayo" : 81000,
    "Junio" : 13000,
    "Julio" : 21000,
    "Agosto" : 41200,
    "Septiembre" : 25000,
    "Octubre" : 21500,
    "Noviembre" : 91000,
    "Diciembre" : 21000,
}

if len(sys.argv) != 2:
    sys.exit(1)

try: 
    umbral = int(sys.argv[1])
except ValueError:
    print("El umbral debe ser un numero entero.")
    sys.exit(1)


#Filtrar los meses que superan el umbral 
ventas_filtradas = {mes: valor for mes, valor in ventas.items() if valor > umbral}

#Resultado
print(ventas_filtradas)



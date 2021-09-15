# Desafío - Ventas
# Patricio Cortés
# G18
# 14-09-2021

# diccionario ventas
ventas = {
"Enero" : 15000 ,
"Febrero" : 22000 ,
"Marzo" : 12000 ,
"Abril" : 17000 ,
"Mayo" : 81000 ,
"Junio" : 13000 ,
"Julio" : 21000 ,
"Agosto" : 41200 ,
"Septiembre" : 25000 ,
"Octubre" : 21500 ,
"Noviembre" : 91000 ,
"Diciembre" : 21000 ,
}

# iterar el diccionario ventas
for i, v in ventas.items():
    if v > 45000:          
        print(i) # imprime solo los meses con ventas mayores que 45000

# Fin del programa
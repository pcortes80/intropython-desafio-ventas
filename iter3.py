# Desafío - Ventas
# Patricio Cortés
# G18
# 14-09-2021

# datos de entrada argv
import sys

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

# define variables
key = [] # lista de keys
value = [] # lista de valores
diccionario_filtrado = {} # nuevo diccionario filrado

# se define el metodo
def filter_dic(dic, par):
    # itera el diccionario ingresado
    for i, v in dic.items():
        if v > par:          
            key.append(i) # agrega keys a la lista key
            value.append(v) # agrega valores a la lista value
    diccionario_filtrado = dict(zip(key,value)) # crea el nuevo diccionario

    # devuelve el nuevo diccionario filtrado
    return diccionario_filtrado 
    
# **** main ****

# Lee la opcion del usuario ingresada y la guarda en la variable "parametro"
parametro = int(sys.argv[1]) # lee el primer argumento del script : parametro

# ejecuta el método
dic = filter_dic(ventas, parametro)
print("El nuevo diccionario filtrado es = ",dic)

# Fin del programa
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

# se define el metodo
def busqueda(dic, par):
    # itera el diccionario ingresado
    for i, v in ventas.items():
        if v == par:          
            return i
            break
          
# **** main ****

# Lee los argumentos ingresados y los guarda en "par1", "par2" y "par3"
par1 = int(sys.argv[1]) # lee el primer argumento
par2 = int(sys.argv[2]) # lee el segundo argumento
par3 = int(sys.argv[3]) # lee el tercer argumento

# ejecuta el método
busqueda1 = busqueda(ventas, par1)
if busqueda1 == None:
    print("no encontrado")
    print("\n")
else:
    print(busqueda1)
    print("\n")

busqueda2 = busqueda(ventas, par2)
if busqueda2 == None:
    print("no encontrado")
    print("\n")
else:
    print(busqueda2)
    print("\n")
    
busqueda3 = busqueda(ventas, par3)
if busqueda3 == None:
    print("no encontrado")
    print("\n")
else:
    print(busqueda3)
    print("\n")
    
# Fin del programa
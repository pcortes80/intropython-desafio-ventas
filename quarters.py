# Desafío - Ventas
# Patricio Cortés
# G18
# 20-09-2021

# datos de entrada argv
import sys

# diccionario ventas vacio
quarters = {}

# Lee el largo del script, para asegurarse de ingresar la cantidad de argumentos correctos
largo = len(sys.argv)

# Solo si la cantidad de argumentos ingresados es correcta se realizan los calculos
if largo > 4:
    # Lee los argumentos ingresados y los guarda
    venta1 = int(sys.argv[1]) # lee el primer argumento
    venta2 = int(sys.argv[2]) # lee el segundo argumento
    venta3 = int(sys.argv[3]) # lee el tercer argumento
    venta4 = int(sys.argv[4])# lee el cuarto argumento
    
    # Ingresa las ventas a cada key
    quarters["Q1"] = venta1
    quarters["Q2"] = venta2
    quarters["Q3"] = venta3
    quarters["Q4"] = venta4
    
    print(quarters)
    
else:
    # Mensaje al usuario
    print("Hay argumentos que faltan. Por favor intente de nuevo.")
  


# Fin de Programa

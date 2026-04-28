def calcular_consumo_tramo(distancia, viento):
    consumo = distancia * 12 
    if viento == "C":
        consumo = consumo * 1.15 
    elif viento == "F":
        consumo = consumo * 0.92
    
    return consumo

reserva_legal = 2000
vuelo_exitoso = True
combustible_actual = float(input("Ingrese el combustible incial en Kg: "))

for tramo in range (1, 6):
    print(f"Inicando tramo {tramo}")
    distancia = float(input("ingrese la distancia del tramo: "))
    viento = input("Tipo de viento (C:contra / F:favor / N:nulo)").upper()
    
    gasto = calcular_consumo_tramo(distancia, viento) 
    
    if (combustible_actual - gasto) < reserva_legal:
        print("ALERTA CRITICA: Combustible insuficiente el siguiente tramo")
        print("Abortando ruta y aterrizando en aeropuerto alterno")
        vuelo_exitoso = False 
        break
    
    combustible_actual = combustible_actual - gasto
    print(f"Combustible restante: {combustible_actual} kg")
    
if vuelo_exitoso == True: 
    print("Vuelo completado con exito")
     
# Capacidad Inicial: El avión despega con un valor de combustible en el tanque en kilogramos.
# 2. Consumo Base: investiga cuál podría ser un consumo estándar en kilogramos por kilómetro.
# 3. Efecto del Viento:
#    - Si hay viento en contra (Headwind), el consumo aumenta en “digamos” un 20%. Este valor, lo debes investigar tú y lo debes justificar. No puede ser el mismo de los otros grupos.
#    - Si hay viento a favor (Tailwind), el consumo se reduce en `otro valor` que investigarás también.
#    - Si el viento es cruzado o nulo, el consumo es el base.
# 4. Reserva Legal: El avión nunca puede bajar de un valor de combustible (este será el límite que tú debes definir). Si al proyectar el siguiente tramo el combustible caerá por debajo de este límite, el sistema debe emitir una alerta crítica, abortar la ruta y aterrizar en el aeropuerto alterno más cercano.

## 1. Se trabajara con un consumo base de 12 kg/km lo que vendria siendo un bimotor tipo Airbus A320 en modo crucero 

## 2. Viento en contra (Headwind) se aumenta el consumo en un 15% lo que vendria siendo un factor 1.15. El avion va a necesitar mas empuje para mantener la velocidad respecto al suelo 

### Viento a favor (Tailwind) este reduce su consumo en un 8% lo que vendria siendo un factor 0.92. El aire empuja la aeronave haciendo asi que se requiera menos potencia 

#### Reserva legal se manejara una de 2000 kg 

#### Tabla de entradas 

|combustible_inicial|cantidad de combustible al despegar |
|distancia_tramo|kilometros a recorrer en el tramo actual|
|tipo_viento| "C"contra, "F"favor,"N"nulo|

#### Tabla de salida

|Consumo_calculado|kilogramos gastados en el tramo|
|combustible_restante|lo que queda en el tanque|
|alerta_critica|mensaje de abortar si cae la reserva|
|resumen_vuelo|mensaje de exito al completar los 5 tramos|

### Tabla de constantes y variables de control 

|Reserva_legal|Constante:limite minimo de segu|
|Consumo_base|Constante:gasto por km sin viento|
|Tramo|V/Control:contador del bucle(1 a 5)|
|Combustible_actual|V/control:si es <= reserva, rompe el ciclo|


### Pseudocodigo 

Funcion calcular_consumo_tramo(distancia, viento)
    consumo = distancia * 12
    Si viento == "C" Entonces
        consumo = consumo * 1.15 // +15%
    Sino Si viento == "F" Entonces
        consumo = consumo * 0.92 // -8%
    FinSi
    Retornar consumo
FinFuncion

Inicio
    combustible_actual = Leer "Combustible inicial"
    RESERVA_LEGAL = 2000
    vuelo_exitoso = Verdadero

    Para tramo = 1 Hasta 5 Con Paso 1 Hacer
        Escribir "Tramo ", tramo
        distancia = Leer "Distancia del tramo"
        viento = Leer "Tipo de viento (C/F/N)"
        
        gasto = calcular_consumo_tramo(distancia, viento)
        
        Si (combustible_actual - gasto) < RESERVA_LEGAL Entonces
            Escribir "ALERTA CRÍTICA: Combustible insuficiente para el siguiente tramo."
            Escribir "Abortando ruta y aterrizando en aeropuerto alterno."
            vuelo_exitoso = Falso
            Break 
        FinSi
        
        combustible_actual = combustible_actual - gasto
        Escribir "Combustible restante: ", combustible_actual
    FinPara

    Si vuelo_exitoso == Verdadero Entonces
        Escribir "¡Vuelo completado con éxito!"
    FinSi
Fin


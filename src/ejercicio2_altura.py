# Ejercicio 2: El guardián de la montaña rusa
#Para subir a la nueva montaña rusa del parque, los visitantes deben medir al menos 150 cm.
#Escribe un programa donde declares una variable altura_visitante (asígnale el valor que quieras). 
#Luego, utiliza un operador relacional para imprimir True si puede subir o False si no puede.

altura_visitante = 180 
altura_minima = 150 

# Evaluar si el visitante puede subir 
puede_subir = altura_visitante >= altura_minima
# Evaluar si cumple con la altura solicitada     
altura_exacta = altura_visitante == 150 

print("¿El visitante puede subir?", puede_subir)
print("¿La altura es 150 cm", altura_exacta)


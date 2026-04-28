# Una universidad otorga becas a los estudiantes si cumplen **alguna** de estas dos condiciones:
# Tener un promedio mayor o igual a 9.0.
# Estar en un nivel socioeconómico nivel 1 y tener un promedio mayor a 8.0.

promedio = 8.5
nivel_socioeconomico = 1

# Condicion 1 
condicion_promedio_alto = promedio >= 9.0 

# Condicion 2 
condicion_socioeconomica = (nivel_socioeconomico == 1) and (promedio > 8.0)

# Evaluacion obtencion beca 
obtiene_beca = condicion_promedio_alto or condicion_socioeconomica 

print("¿cumple con la condicion del promedio alto?", condicion_promedio_alto)
print("¿cumple con la condicion socioeconomica?" , condicion_socioeconomica)
print("¿Obtiene la beca?", obtiene_beca)
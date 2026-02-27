# Imagina que fuiste a cenar con 3 amigos (son 4 en total). La cuenta fue de $85. Además, quieren dejar un 15% de propina.
# Escribe un programa en Python que calcule:

**Codigo** 
```py
Personas = 4 
Cuenta = 85
Propina = 0.15 

# Total de la propina 
Total_propina = Cuenta * Propina

# Total a pagar 
Total_cuenta = Total_propina + Cuenta 

# Parte de cada persona: partes iguales 
Partes_iguales = Total_cuenta / Personas

print("Total de la propina es:" , Total_propina)
print("El total de la cuenta con la propina es:" , Total_cuenta)
print("Le corresponde a cada uno:" , Partes_iguales)
```

**Captura pantalla** 
![Ejercicio1](images/Ejercicio1_arimetica.png)

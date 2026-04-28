# Ejercicio 1 
# Comprueba en la consola de Python los siguientes códigos

```py 
print(10 > 5)
print("Hola" != "Mundo")
print(3.14 <= 4.5)
nombre = "Juan"
print(nombre == "Juan")
```
# Ejercicio 2
# Resuelve el siguiente problema usando el condicional simple.
# Un almacén cobra `$9 000` por costos de envío, pero ofrece el envío a domicilio gratis para compras superiores a `$100 000`. En caso contrario, no hay ningún descuento. Solicite al usuario el valor de la compra y calcule el valor total a pagar.

```py 

valor_compra = int(input("ingrese el valor de la compra: "))
costo_envio = 9000

if valor_compra > 100000:
    costo_envio = 0

total_pagar = valor_compra + costo_envio 

print("costo de envio:", costo_envio)
print("total a pagar:" total_pagar)
```

# Ejercicio 3
# Determine si un número ingresado por el usuario es par o impar.

```py
numero = int(input("Ingrese un número entero: "))

residuo = numero % 2

if residuo != 0:
    print(f"El número {numero} es impar")
else:
    print(f"El número {numero} es par")
```

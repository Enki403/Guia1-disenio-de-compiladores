# Ejercicios de 'Guía 1' - Diseño de compiladores

## Instalación de dependencias
El proyecto utiliza PyQt5 y pandas, para instalar estas dependencias automáticamente puedes hacer uso de `pip` con la sentencia: `pip install -r requirements.txt`

## Grupo 1
**Integrantes**:
- Alexis Ochoa
- Hector Vasquez
- Jose Barrientos
- Josue Caballero
- Melissa Diaz
- Nora Rodriguez

## Contenido
### Ejercicio 1 ('Calculadora')
Elabore una calculadora en Python que realice las operaciones de sumar, restar, multiplicar, dividir, calcule la raíz cuadrada. Considere las entradas de solo números (enteros y decimales sin el uso de “e”).

### Ejercicio 2 ('Conversor')
Elabore un convertidor de números donde se puede seleccionar la opción de entrada (binario, octal, decimal y hexadecimal) se ingrese el valor y después se seleccione una salida (binaria, octal, decimal o hexadecimal).

### Ejercicio 3 ('Analizador')
<![endif]-->

Elabore un script donde se puede leer un archivo de texto y que identifique un patrón, cuando hay una secuencia de números (1 o más números), donde haya una secuencia de números y letras (1 o más números seguidos de 1 o más letras), un patrón donde identifique letras que contengan un más de tres vocales iguales (por ejemplo: _palabra_ o _aab3a_; tienen 3 vocales **a**, emisión o _oaaee_ solo tiene 2  vocales **i** em**i**s**i**on, 2 vocales **a**, 2 vocales **e**; por lo cual no cumple la condición), y por último que identifique si hay un carácter especial en la entrada (por ejemplo ssdsdk&sd* donde se encontró & y *). Haga uso de la biblioteca de Python para identificar patrones.

La salida debe mostrar un arreglo impreso de las ocurrencias encontradas o dar un mensaje que no encontró ninguna. De forma opcional puede mandar la salida en un txt o un archivo de Excel.
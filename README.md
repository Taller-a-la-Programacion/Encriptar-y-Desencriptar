# Encriptar y Desencriptar Documentos

## 1.	Encriptar
### 1.1.	Instrucciones generales
-	Debe de estar en un archivo llamado **encriptar.py**
-	La función principal debe llamarse **encriptarArchivo(archivo, archivoSalida)**
-	Debe existir una función llamada **encriptar(texto)**, donde texto es un parámetro tipo String y retornará un String encriptado
### 1.2.	Descripción de la actividad
Dado un archivo plano, encriptar su contenido, para ello tomar cada caracter del texto y convertirlo a su representación hexadecimal para ello primero debe convertir cada uno de ellos a su valor Unicode y posteriormente a su valor hexadecimal. Para ello podrá hacer del uso de la función ord(), por ejemplo:
```python
>>>ord(“A”)
65
>>>convertDecAHex(65)
41
```
Ahora encriptando una palabra, por ejemplo **“CASA”**
-	Obteniendo cada uno de los valores Unicode de cada letra 
-	C= 67 A=65 S=83 A=65
-	Cada valor Unicode, convertir a hexadecimal
-	C=043 A=041 S=053 A=041
Entonces el valor encriptado de CASA sería 043041053041
Cada carácter que se convierta a hexadecimal tendrá un largo de 3, por ejemplo, convertir hexadecimal 67 es 43, pero lo representamos como 043.
## 2.	Desencriptar:
### 2.1.	Instrucciones generales
-	Debe de estar en un archivo llamado **desencriptar.py**
-	La función principal debe llamarse **desencriptarArchivo(archivo, archivoSalida)**
-	Debe existir una función llamada **desencriptar(texto)**, donde texto es un parámetro tipo String y retornará un String desencriptado
### 2.2.	Descripción de la actividad
Dado un archivo plano, desencriptar su contenido, para ello tomar cada conjunto de tres caracteres de texto y convertirlo de su representación hexadecimal a su valor Unicode y posteriormente a su representación caracter haciendo uso de la función chr(). Para ello podrá hacer del uso de la función chr(), por ejemplo:
```python
>>>convertHexADec(“041”)
65
>>>chr(65)
“A”
```
Ahora desencriptando, por ejemplo “043041053041”
-	Obteniendo cada 3 caracteres que sería la representación hexadecimal de cada carácter, 
-	C=“043” A=”041” S=”053” A=”041”
-	Cada valor hexadecimal, convertir a Unicode
-	C= 67 A=65 S=83 A=65
-	Y cada uno de estos valores usar función chr()
Entonces el valor encriptado de “043041053041” sería CASA 

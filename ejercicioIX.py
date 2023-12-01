#!/usr/bin/python3

cad = input("Introduce una cadena: ")
subcad = input("Introduce una subcadena: ")

if cad.find(subcad) > -1:
	print("La cadena contiene la subcadena.")
else:
	print("La cadena no contiene la sucadena")

# hecho de otra forma 

if subcad in cad:
	print("La cadena contiene la subcadena.")
else:
	print("La cadena no contiene la subcadena.")


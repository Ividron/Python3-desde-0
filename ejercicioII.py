#!/usr/bin/python3

#cadenas de caracteres

cad = input("Introduce una cadena: ")
subcad = input("Introduce una subcaden: ")
if cad.startswith(subcad):
	print("La cadena comienza por la subcadena")
else:
	print("La cadena NO comienza por la subcadena")

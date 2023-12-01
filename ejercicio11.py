#!/usr/bin/python3

es_primo = True
numero_es_primo = int(input("Introduce un número para comprobar si es primo:"))
for num in range(2, numero_es_primo):
	if numero_es_primo % num == 0:
		es_primo = False
		break

if es_primo:
	print("Es Primo")
else:
	print("No es primo")

#!/usr/bin/python3

def esmultiplo(num1,num2):
	if num1 % num2 == 0:
		return True
	else:
		return False

numero1 = int(input("Número 1:"))
numero2 = int(input("Número 2:"))
if esmultiplo(numero1,numero2):
	print(numero1,"es múltiplo de",numero2)
else:
	print(numero1,"no es múltiplo de",numero2)

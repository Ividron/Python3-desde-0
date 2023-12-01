#!/usr/bin/python3

suma = 0
cont = 0

while True:
        num=int(input("Número (0 para salir): "))
        suma = suma + num
        cont = cont + 1

        if num !=0:
                cont = cont + 1
        if num == 0:
                break

if cont != 0:
        media = suma / cont
else:
        media = 0

print("Suma:", suma)
print("Media:", media)

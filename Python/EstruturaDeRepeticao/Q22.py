#!/usr/bin/env python3

#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

contador=0
divisores=[]
numero=int(input("Digite o número: "))
if numero!=-1 and numero!=0 and numero!=1:
    for divisor in range(1,numero+1):
        if numero%divisor==0:
            contador+=1 #O contador aumenta quando há um divisor
            divisores.append(divisor)
    if contador>2:
        print(numero,"não é um número primo")
        print("Divisores",divisores)
    else:
        print(numero,"é um número primo")
else:
    print(numero,"não é um número primo")  

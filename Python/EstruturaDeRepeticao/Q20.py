#!/usr/bin/env python3

#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

resposta="SIM"
while resposta=="SIM":
    fatorial=1
    num=int(input("\nDigite o número: "))
    if 0<num<16:
        for i in range(1,num+1,1):
            fatorial=fatorial*i
        print("Fatorial de",num,"é igual a",fatorial)
    else:
        print("\nOs números devem ser positivos e menores que 16")        
    resposta=input("\nDigite SIM para continuar: ").upper()

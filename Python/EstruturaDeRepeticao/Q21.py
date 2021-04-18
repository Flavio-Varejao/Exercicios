#!/usr/bin/env python3

#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

#VERSÃO COM CONTADOR

contador=0
numero=int(input("Digite o número: "))
if numero!=-1 and numero!=0 and numero!=1:
    for divisor in range(1,numero+1):
        if numero%divisor==0:
            contador+=1 #O contador aumenta quando há um divisor
    if contador>2:
        print(numero,"não é um número primo")
    else:
        print(numero,"é um número primo")
else:
    print(numero,"não é um número primo")  

#VERSAO COM LISTA

#lista=[]
#numero=int(input("Digite o número: "))
#if numero!=-1 and numero!=0 and numero!=1:
    #for divisor in range(1,numero+1):
        #if numero%divisor==0:
            #lista.append(divisor)
    #if len(lista)>2:
        #print(numero,"não é um número primo")
    #else:
        #print(numero,"é um número primo")
#else:
    #print(numero,"não é um número primo")          
'''
A lista possui apenas divisores do número digitado
Se a lista tiver mais de 2 divisores, além do número 1 e dele mesmo, significa que ele não é primo, pois um número primo só é divisível por 1 e por ele mesmo
'''

#!/usr/bin/env python3

'''
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

Altere o programa anterior para mostrar no final a soma dos números.
'''

#FOR
lista=[]
for num in range(int(input("Digite o 1º número: "))+1,int(input("Digite o 2º número: ")),1):
    lista.append(num)
print("lista = "+str(lista))
print("soma = "+str(sum(lista)))

#WHILE
#lista=[]
#num1=int(input("Digite o 1º número: "))
#num2=int(input("Digite o 2º número: "))-1
#while num1<num2:
    #num1+=1
    #lista.append(num1)
#print("lista = "+str(lista))
#print("soma = "+str(sum(lista)))

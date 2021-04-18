#!/usr/bin/env python3

#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1

num=int(input("Digite o número: "))
fatorial=1
for i in range(1,num+1,1):
    fatorial=fatorial*i
print("Fatorial de",num,"é igual a",fatorial)

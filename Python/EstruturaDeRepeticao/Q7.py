#!/usr/bin/env python3

#Faça um programa que leia 5 números e informe o maior número.

#Exemplo com FOR
lista=[]
for num in range(0,5,1):
    lista.append(int(input("Digite o número: ")))
print("O maior número digitado é: "+str(max(lista)))

#Exemplo com WHILE
#lista=[]
#while len(lista)<5:
    #lista.append(input("Digite o numero: "))
#print("O maior numero digitado é: "+str(max(lista)))

#!/usr/bin/env python3

#Faça um programa que leia 5 números e informe a soma e a média dos números.

#FOR
lista=[]
for num in range(0,5,1):
    lista.append(int(input("Digite o número: ")))
print("soma = "+str(sum(lista)))
print("media = "+str(sum(lista)/len(lista)))

#WHILE
#lista=[]
#while len(lista)<5:
    #lista.append(int(input("Digite o número: ")))
#print("soma = "+str(sum(lista)))
#print("media = "+str(sum(lista)/len(lista)))

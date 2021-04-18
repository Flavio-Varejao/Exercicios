#!/usr/bin/env python3

#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

lista=[]
pares=[]
impares=[]

for num in range(0,10,1):
    lista.append(int(input("Digite um número: ")))
for i in lista:
    if i%2==0:
        pares.append(i)
    else:
        impares.append(i)
print("\n"+str(len(pares)),"número(s) par(es):")
print(pares)
print("\n"+str(len(impares)),"número(s) ímpar(es):")
print(impares)


#print(lista)
#print("Números pares: "+str(len(pares)))
#print("Números ímpares: "+str(len(impares)))

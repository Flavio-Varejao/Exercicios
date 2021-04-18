#!/usr/bin/env python3

'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
'''

num1=int(input("Digite a base da potência: "))
num2=int(input("Digite o expoente da potência: "))
potencia=num1**num2
#print(num1,"elevado a",num2,"=",potencia)
print(str(num1)+" elevado a "+str(num2)+" = "+str(potencia))

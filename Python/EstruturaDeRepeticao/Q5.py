#!/usr/bin/env python3
'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''
pop_a=int(input("Digite a população inicial do país A: "))
while pop_a < 80000:
    pop_a=int(input("\nA população de A deve ser maior que 80000 habitantes"
        "\nDigite a população inicial do país A: "))
pop_b=int(input("\nDigite a população inicial do país B: "))
while pop_b < 200000:
    pop_b=int(input("\nA população de B deve ser maior que 200000 habitantes"
              "\nDigite a população inicial do país A: "))
taxa_a=float(input("\nDigite a taxa de crescimento anual de A: "))
while taxa_a < 3:
    taxa_a=float(input("\nA taxa de crescimento deve ser maior que 3%: "))
taxa_b=float(input("\nDigite a taxa de crescimento anual de B: "))
while taxa_b < 1.5:
    taxa_b=float(input("\nA taxa de crescimento deve ser maior que 1.5%: "))
    
ano = 0

while pop_a <= pop_b:
    pop_a += pop_a * taxa_a/100
    pop_b += pop_b * taxa_b/100
    ano += 1

print ( "\nA ultrapassa ou iguala a B em %d anos" %ano )

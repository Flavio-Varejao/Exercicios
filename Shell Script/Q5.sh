#!/usr/bin/env bash

# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
# 
# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.

read -rp "Digite a população inicial do país A: " pop_a
while [ "$pop_a" -lt 80000 ]; do
    echo -en "\nA população de A deve ser maior que 80000 habitantes"
        "\nDigite a população inicial do país A: "; read -r pop_a
done
read -rp "Digite a população inicial do país B: " pop_b
while [ "$pop_b" -lt 200000 ]; do
    echo -en "\nA população de B deve ser maior que 200000 habitantes"
        "\nDigite a população inicial do país B: "; read -r pop_b
done
echo -en "\nDigite a taxa de crescimento anual de A: "; read -r taxa_a
while [ "$taxa_a" -lt 3 ]; do
    echo -en "\nA taxa de crescimento deve ser maior que 3%: "; read -r taxa_a
done
echo -en "\nDigite a taxa de crescimento anual de B: "; read -r taxa_b
while [ "$taxa_b" -lt 1.5 ]; do
    echo -en "\nA taxa de crescimento deve ser maior que 1.5%: "; read -r taxa_b
done

ano=0
while [ "$pop_a" -le "$pop_b" ]; do
    let pop_a=pop_a*(taxa_a/100)
    let pop_b=pop_b*(taxa_b/100)
    let ano+=1
done
echo "A ultrapassa B em $ano anos" 

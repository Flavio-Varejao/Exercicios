#!/usr/bin/env bash

#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

contador=0
while ((contador < 10)); do
    read -rp "Digite um número: " lista[contador]
    ((contador+=1))
done
for numero in "${lista[@]}"; do
    if [ $((numero%2)) = 0 ]; then
        pares+=("$numero")
    else
        impares+=("$numero")
    fi
done
echo "${#pares[*]} número(s) par(es): ${pares[*]}"
echo "${#impares[*]} número(s) ímpar(es): ${impares[*]}"

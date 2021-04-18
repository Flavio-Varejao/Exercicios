#!/usr/bin/env bash

#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

contador=0
echo -e "Verifique se um número é primo\n"
read -rp "Digite um número: " numero
if [ "$numero" -ne -1 ] && [ "$numero" -ne 0 ] && [ "$numero" -ne 1 ]; then
    for divisor in $(seq "$numero"); do
        if [ $((numero%divisor)) == 0 ]; then
            contador=$((contador+1))
        fi
    done    
    if [ "$contador" -gt 2 ]; then
        echo "$numero não é um número primo"
    else
        echo "$numero é um número primo"
    fi
else
    echo "$numero não é um número primo"
fi

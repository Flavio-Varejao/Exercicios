#!/usr/bin/env bash

#Faça um programa que leia 5 números e informe o maior número.

maior=0; contador=0
while ((contador < 5)); do
    echo -n "Digite um número: "; read lista[contador]
    let contador++
    for numero in ${lista[@]}; do
        if [ $numero -gt $maior ]; then
            maior=$numero
        fi
    done
done
echo ${lista[@]} #lista=("$num1" "$num2" "$num3" "$num4" "$num5")
echo "O maior número é $maior"

#!/usr/bin/env bash

#Faça um programa que leia 5 números e informe a soma e a média dos números.

contador=0; soma=0
while ((contador < 5)); do
    echo -n "Digite um número: "; read lista[contador]
    let contador++
done
for numero in ${lista[@]}; do
    soma=$((soma+numero))
done
echo "${lista[@]}"
echo "Soma = $soma"
echo "media = $((soma/${#lista[@]}))"

# for numero in ${lista[@]}; do
#     let soma+=$numero
# done

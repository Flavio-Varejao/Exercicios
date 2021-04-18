#!/usr/bin/env bash

# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
# Altere o programa anterior para mostrar no final a soma dos números.

soma=0
read -rp "Digite o número inicial: " num1
read -rp "Digite o número final: " num2

for ((numero=$((num1+1)); numero<num2; numero++)); do
    lista+=$numero" "
done
for num in in ${lista[@]}; do
    soma=$((soma+num))
done
echo "${lista[@]}"
echo "Soma = $soma"

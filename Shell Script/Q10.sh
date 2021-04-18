#!/usr/bin/env bash

#Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

read -rp "Digite o número inicial: " num1
read -rp "Digite o número final: " num2

for ((numero=$((num1+1)); numero<num2; numero++)); do
    echo "$numero"
done

#!/usr/bin/env bash

#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1

read -rp "Digite um número inteiro: " num
fatorial=1
for ((numero=1; numero<=num; numero++)); do
    fatorial=$((fatorial*numero))
done
echo "Fatorial de $num é $fatorial"

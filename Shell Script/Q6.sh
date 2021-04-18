#!/usr/bin/env bash

#Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.

#números um abaixo do outro

for ((numero=1;numero<=20;numero++)); do
    echo $numero
done

#números um ao lado do outro

for ((numero=1;numero<=20;numero++)); do
    lista+=$numero" "
done
echo "$lista"

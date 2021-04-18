#!/usr/bin/env bash

#Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.

for ((numero=1; numero<=50; numero++)); do
    if [ $((numero%2)) != 0 ]; then
        echo "$numero"
    fi
done

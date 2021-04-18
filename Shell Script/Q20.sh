#!/usr/bin/env bash

#Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

resposta="S"
fatorial=1
while [ "$resposta" = "S" ]; do
    echo -en "\nDigite um número inteiro: "; read -r num
    if [ "$num" -le 0 ] || [ "$num" -ge 16 ]; then
        echo -en "\nO número precisa ser maior que 0 e menor que 16"
    else
        for ((numero=1; numero<=num; numero++)); do
            fatorial=$((fatorial*numero))
        done
        echo "Fatorial de $num é $fatorial"
    fi  
    echo -en '\nDigite "S" para continuar: '; read -r resposta && resposta=${resposta^^}
done


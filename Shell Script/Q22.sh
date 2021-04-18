#!/usr/bin/env bash

#Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.

contador=0
echo -e "Verifique se um número é primo\n"
read -rp "Digite um número: " numero
if [ "$numero" -ne -1 ] && [ "$numero" -ne 0 ] && [ "$numero" -ne 1 ]; then
    for divisor in $(seq "$numero"); do
        if [ $((numero%divisor)) == 0 ]; then
            contador=$((contador+1))
            divisores+=("$divisor")
        fi
    done    
    if [ "$contador" -gt 2 ]; then
        echo "$numero não é um número primo"
        echo "Divisores: ${divisores[*]}"
    else
        echo "$numero é um número primo"
    fi
else
    echo "$numero não é um número primo"
fi

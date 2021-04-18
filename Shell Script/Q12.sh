#!/usr/bin/env bash

# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.

read -rp "Digite o número: " num
echo -e "\nTabuada do número $num:"

for ((numero=1; numero<=10; numero++)); do
    echo "$num x $numero = $((num*numero))"
done

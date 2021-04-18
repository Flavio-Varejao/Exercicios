#!/usr/bin/env bash
 
# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

read -rp "Digite o nome: " nome
while [ "$(echo "${#nome}")" -lt 4 ]; do
    read -rp "O nome deve ter mais de 3 caracteres: " nome
done
read -rp "Digite a idade: " idade
while [ "$idade" -lt 1 ] || [ "$idade" -gt 150 ]; do
    read -rp "A idade deve ser entre 0 e 150: " idade
done
read -rp "Digite o salário: " salario
while [ "$salario" -lt 1 ]; do
    read -rp "O salario deve ser maior que 0: " salario
done
read -rp "Digite o seu gênero: " genero; genero=${genero^^}
while [ "$genero" != "F" ] && [ "$genero" != "M" ]; do
    read -rp "Digite 'F' para feminino ou 'M' para masculino: " genero; genero=${genero^^}
done
read -rp "Digite o estado civil: " estadoCivil; estadoCivil=${estadoCivil^^}
while [ "$estadoCivil" != "S" ] && [ "$estadoCivil" != "C" ] && [ "$estadoCivil" != "V" ] && [ "$estadoCivil" != "D" ]; do
    read -rp "Digite 'S' para solteiro, 'C' para casado(a), 'V' para viuvo(a) ou 'D' para divorciado(a): " estadoCivil; estadoCivil=${estadoCivil^^}
done

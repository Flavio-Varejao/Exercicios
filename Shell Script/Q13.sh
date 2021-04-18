#!/usr/bin/env bash

# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.

read -rp "Digite a base da potência: " base
read -rp "Digite o expoente da potência: " expoente
potencia=$(bc <<< "$base^$expoente")
echo "Resultado de $base elevado a $expoente = $potencia"

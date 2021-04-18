#!/usr/bin/env bash

# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

read -E -rp "\nDigite uma nota: " nota
while [ "$nota" -lt 0 ] || [ "$nota" -gt 10 ]; do
    read -rp "Digite uma nota entre 0 e 10: " nota
done

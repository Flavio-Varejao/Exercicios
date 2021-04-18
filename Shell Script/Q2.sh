#!/usr/bin/env bash

#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

echo -en "\nDigite o usuário: "; read usuario
echo -n "Digite a senha: "; read -s senha
while [ "$usuario" = "$senha" ]; do
    echo -e "\nUsuário e senha não podem ser iguais"
    echo -en "\nDigite o usuário: "; read usuario
    echo -n "Digite a senha: "; read -s senha
done

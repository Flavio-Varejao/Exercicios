#!/usr/bin/env python3

#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome=input("Digite seu nome de usuário: ")
senha=input('Digite sua senha: ')
while nome==senha:
    print("\nErro! O nome de usuário e senha não devem ser iguais")
    nome=input("\nDigite seu nome de usuário: ")
    senha=input('Digite sua senha: ')

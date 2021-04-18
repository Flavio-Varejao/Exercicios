#!/usr/bin/env python3

'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''
nome=input("Digite o seu nome: ")
while len(nome)<4:
    nome=input("O nome deve ter mais de 3 caracteres: " )
idade=int(input("Digite sua idade: "))
while idade<0 or idade>150:
    idade=int(input("A idade deve ser entre 0 e 150: "))
salario=float(input("Digite seu salário: "))
while salario<0:
    salario=float(input("O salário deve ser um número positivo: "))
genero=input("Digite o seu sexo: ").upper()
while genero!="M" and genero!="F":
    genero=input("Digite 'F' para feminino ou 'M' para masculino: ").upper()
estadoCivil=input("Digite seu estado civil: ").upper()
while estadoCivil!="S" and estadoCivil!="C" and estadoCivil!="V" and estadoCivil!="D":
    estadoCivil=input("Digite 'S' para solteiro(a), 'C' para casado(a), 'V' para viúvo(a) ou 'D' para divorciado(a): ").upper()

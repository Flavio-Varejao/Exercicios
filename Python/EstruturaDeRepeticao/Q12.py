#!/usr/bin/env python3

'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.
'''

numero=int(input("Digite o número: "))
print("Tabuada de " +str(numero)+":")
for num in range(1,11,1):
    tabuada=numero*num
    print('{Numero} x {Num} = {Tabuada}'.format(Numero=numero,Num=num,Tabuada=tabuada))

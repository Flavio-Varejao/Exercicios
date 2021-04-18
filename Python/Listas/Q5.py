'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
'''
numeros=[]
par=[]
impar=[]
for numero in range(1,21):
    numeros.append(numero)
    if numero%2 == 0:
        par.append(numero)
    else:
        impar.append(numero)
print("Números totais:",numeros)
print("Números ímpares:",impar)
print("Números pares:",par)


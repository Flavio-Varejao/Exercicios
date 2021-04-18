'''
Faça um Programa que leia um vetor de 5 números inteiros, 
mostre a soma, a multiplicação e os números.
'''

numeros=[]
multi=1
for numero in range(1,6):
    numeros.append(int(input("Digite um número: ")))
for numero in numeros:
    multi=multi*numero

print("Números:",numeros)
print("Multiplicação:",multi)
print("Soma:",sum(numeros))


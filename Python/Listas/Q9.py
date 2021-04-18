'''
Faça um Programa que leia um vetor A com 10 números inteiros,
calcule e mostre a soma dos quadrados dos elementos do vetor.
'''
A=[]
B=[]
for numero in range(10,21):
    A.append(numero)
for numero in A:
    B.append(numero*numero)
   
print("Vetor A:",A)            
print("Vetor quadrado de A:",B)
print("Soma dos quadrados dos elementos do vetor A:",sum(B))

#OU

""" 
A=[]
for numero in range(10,21):
    A.append(numero)
B=[numero*numero for numero in A]

print("Vetor A:",A)            
print("Vetor quadrado de A:",B)
print("Soma dos quadrados dos elementos do vetor A:",sum(B))
"""

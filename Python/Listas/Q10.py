'''
Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão 
ser compostos pelos elementos intercalados dos dois outros vetores.
'''
A=[numero for numero in range(1,11)]
B=[numero for numero in range(11,22)]
C=[*sum(zip(A,B),())]

print("Vetor A:",A)
print("Vetor B:",B)
print("Vetor intercalado de A e B:",C)
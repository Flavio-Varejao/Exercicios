'''
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
'''

lista1=[]
lista2=[]
for numero in range(1,11):
    lista1.append(float(input("Digite um número: ")))
for numero in reversed(lista1):
    lista2.append(numero)
print(lista2)
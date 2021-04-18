'''
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. 
Imprima as consoantes.
'''
letras=[]
consoantes=[]

for letra in range(1,11):
    letras.append(input("Digite uma letra: ").upper())
for caractere in letras:
    if caractere != "A" and caractere != "E" and caractere != "I" and caractere != "O" and caractere != "U":
        consoantes.append(caractere)

print("Foram lidas",len(consoantes),"consoantes")
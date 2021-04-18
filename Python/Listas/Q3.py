'''
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''
notas=[]

for nota in range(1,5):
    notas.append(float(input("Digite uma nota: ")))

media=sum(notas)/len(notas)

print("Notas",notas)
print("Média",media)

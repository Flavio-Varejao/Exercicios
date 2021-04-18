'''
Faça um Programa que peça as quatro notas de 3 alunos, 
calcule e armazene num vetor a média de cada aluno, 
imprima o número de alunos com média maior ou igual a 7.0.
'''
notas={}
medias=[]
contador=0
for nota in range(1,4):
    nome=input("\nDigite o seu nome: ")
    notas[nome]=[
        float(input("Digite a 1ª nota: ")),
        float(input("Digite a 2ª nota: ")),
        float(input("Digite a 3ª nota: ")),
        float(input("Digite a 4ª nota: "))]
for nome,nota in notas.items():
    medias.append(sum(nota)/4)
for media in medias:
    if media >= 7:
        contador+=1
print("\nNotas dos alunos:\n",notas)
print("Médias dos alunos:\n",medias)
print("Alunos com média maior ou igual a 7:",contador)
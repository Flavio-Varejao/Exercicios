'''
Faça um Programa que peça a idade e a altura de 3 pessoas, 
armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
'''
pessoas={}
for pessoa in range(1,4):
    chave=input("\nDigite o seu nome: ")
    pessoas[chave]=[
        int(input("Digite a sua idade: ")),
        float(input("Digite a sua altura: "))]
for chave,pessoa in reversed(pessoas.items()):
    print(chave,pessoa)
'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
O programa deve ser encerrado quando não for informado o nome do atleta.
'''
atletas={}
nomes=[]
resp="S"
while resp=="S":
    nomes.append(input("\nDigite o nome do atleta: "))
    resp=input("\nDigite <S> para continuar: ").upper()

for nome in range(0,len(nomes)):
    print("\nAtleta:",nomes[nome])
    atletas[nomes[nome]]=[float(input("Digite o primeiro salto: ")),\
                float(input("Digite o segundo salto: ")),\
                float(input("Digite o terceiro salto: ")),\
                float(input("Digite o quarto salto: ")),\
                float(input("Digite o quinto salto: "))]

for chave,saltos in atletas.items():
    media=sum(saltos)/len(saltos)
    print("\nAtleta:",chave)
    print("\nPrimeiro salto:",saltos[0],"m")
    print("Segundo salto:",saltos[1],"m")
    print("Terceiro salto:",saltos[2],"m")
    print("Quarto salto:",saltos[3],"m")
    print("Quinto salto:",saltos[4],"m")
    print("\nResultado final:")
    print("Atleta:",chave)
    print("Saltos:",saltos[0],"-",saltos[1],"-",saltos[2],"-",saltos[3],"-",saltos[4])
    print("Média dos saltos:",media,"m")
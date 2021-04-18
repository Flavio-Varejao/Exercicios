'''
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
Após isto, calcule a média anual das temperaturas e mostre todas as 
temperaturas acima da média anual, e em que mês elas ocorreram 
(mostrar o mês por extenso: 1 – Janeiro,
2 – Fevereiro, . . . ).
'''

# temperaturas={'jan':20,'fev':30}
temperaturas={}

resp="S"
while resp == "S":
    chave=input("\nDigite o mês do ano: ").upper()
    temperaturas[chave]=int(input("Digite a temperatura média do mês: "))
    resp=input("\nDigite S para continuar: ").upper()

print("\nTemperaturas acima da média anual:\n")
# values() recupera os valores de cada chave
media=sum(temperaturas.values())/len(temperaturas.values()) 
for chave,temperatura in temperaturas.items():
    if temperatura > media:
        print(chave,temperatura,"graus")

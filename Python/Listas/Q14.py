'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação 
sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 
questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 
5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
'''
contador=0
perguntas=[input("Telefonou para a vítima? ").upper(),
            input("Esteve no local do crime? ").upper(),
            input("Mora perto da vítima? ").upper(),
            input("Devia para a vítima? ").upper(),
            input("Já trabalhou com a vítima? ").upper()]
for resposta in perguntas:
    if resposta == "S":
        contador+=1
if contador == 0 or contador == 1:
    print("\nVocê é inocente")
elif contador == 2:
    print("\nVocê é suspeito")
elif contador == 3 or contador == 4:
    print("\nVocê é cúmplice")
else:
    print("\nVocê é o assassino")
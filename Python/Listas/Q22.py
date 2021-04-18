mouses={'1':0,'2':0,'3':0,'4':0}
resposta=1
while resposta != "0":
    opcao=input("\nEscolha uma opção:\n"+
            "<1> - Necessita de esfera\n"+
            "<2> - Necessita de limpeza\n"+
            "<3> - Necessita trocar do cabo ou conector\n"+
            "<4> - Quebrado ou inutilizado: ")
    if opcao == "1":
        print("\nNecessita de esfera")
        mouses['1']=int(input("Digite a quantidade: "))
    elif opcao == "2":
        print("\nNecessita de limpeza")
        mouses['2']=int(input("Digite a quantidade: "))
    elif opcao == "3":
        print("\nNecessita trocar do cabo ou conector")
        mouses['3']=int(input("Digite a quantidade: "))
    elif opcao == "4":
        print("\nQuebrado ou inutilizado")
        mouses['4']=int(input("Digite a quantidade: "))
    else:
        break
    
    resposta=input("\nDigite <0> para sair: ")

print("\nQuantidade de mouses:",sum(mouses.values()))
print("\nSituação                               Quantidade       Percentual")
print("1 - necessita da esfera                  ",mouses['1'],"             ",mouses['1']/sum(mouses.values()))
print("2 - necessita de limpeza                 ",mouses['2'],"             ",mouses['2']/sum(mouses.values()))
print("3 - necessita troca do cabo ou conector  ",mouses['3'],"             ",mouses['3']/sum(mouses.values()))
print("4 - quebrado ou inutilizado              ",mouses['4'],"             ",mouses['4']/sum(mouses.values()))
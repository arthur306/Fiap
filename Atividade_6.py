#---Orientações---

#Logística: controle de estoque
#Problema: falta de controle de insumos
#Soluções: Cadastro de produtos, controle de entrada/saída e alerta de estoque baixo
#py: Listas/dicionários, Json e txt, oracle 

#---Código---

lista_produtos = list()
lista_quantidade = list()
#Funções subalgoritmo:
def cadastrar():
    nome = str(input("Digite o nome do produto:"))
    quantidade = int(input("Quantidade do produto:"))
    lista_produtos.append(nome)
    lista_quantidade.append(quantidade)
    print("Produtos cadastrados com sucesso.")
    
def adicinar():
    print(lista_produtos)
    nome = str(input("Digite o nome do produto para adicionar:\n"))
    if nome in lista_produtos:
        indice = lista_produtos.index(nome)
        qtd = int(input("Quantidade a adicionar: "))
        lista_quantidade[indice] += qtd
        print("Quantidade adicionada com sucesso.")
    else:
        print("Produno inexistente.")
def retirar():
    print(lista_produtos)
    nome = str(input("Digite o nome do produto para adicionar:\n"))
    if nome in lista_produtos:
        indice = lista_produtos.index(nome)
        qtd = int(input("Quantidade a retirar: "))
        if lista_quantidade[indice] >= qtd:
            lista_quantidade[indice] -= qtd
            print("Quantidade retirada com sucesso.")
        else:
            print("Quantidade insuficiente.")
    else:
        print("Produto não encontrado.")    
def verificar():
    dicionario = dict(zip(lista_produtos, lista_quantidade))
    while True:
          try:
              verificacao = int(input("\nEscolha o que quer fazer:\n"
                                      "1_Verificar produtos\n"
                                      "2_Voltar"))
          except:
                print("Digite apenas números, por favor.")
                continue
          match verificacao:
                case 1:
                    print("\n---Produtos---\n")
                    for produto, quantidade in dicionario.items():
                        print(f"{produto}: {quantidade}")
                case 2:
                    break
                
                case _:
                    print("Opção inválida.")
                    
#Menu subalgoritmo:

def menu():
    while True:
        try:
            escolha = int(input("\nSelecione uma das opções:\n"
                                "1_Cadastro de Produtos\n" 
                                "2_Adicionar aos Produtos existentes\n"
                                "3_Retirar dos produtos existentes\n"
                                "4_Verificar produtos\n"
                                "5_Encerrar sistema\n"))
        except: 
            print("Digite apenas números, por favor.")
            continue
        match escolha:
            case 1:
                cadastrar()
            case 2:
                adicinar()
            case 3:
                retirar()
            case 4:
                verificar()
            case 5:
                print("Encerrando o sistema")
                break
            case _:
                print("Opção inválida")

                      
import json
#Menu
print("===Bem-vindo ao gerenciador de estoques agrônomos===")
menu()

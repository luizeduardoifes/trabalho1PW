# while True:
#     print("ESCOLHA UMA FORMA DE SALVAR OS DADOS:\n1- Cadastrar Produtos\n2-Listar Produtos\n3- Sair")
#     escolha = int(input(""))
#     lista = []
#     if escolha == 1:
#         produto = input("Digita o nome do produto: ")
#         preco = float(input("digita o preco do produto: "))

#         dicionario = {"Nome do Produto" : produto, "Preco do Produto" : preco}
#         if produto == dicionario["Nome do Produto"]:
#             print("Produto nao cadastrado")
            
#         else:
#             lista.append(dicionario)
#             print("cadastrado com sucesso")
#             a = input("deseja continuar?")
#             if a == "sim":
#                 produto = input("Digita o nome do produto: ")
            
        



        
            

# ex3.x :: Faça um programa que solicite continuamente ao usuário a digitação do nome, preço e estoque de um produto, salvando os dados em 3 coleções separadas, sendo que o nome do produto não pode se repetir. O programa deve oferecer 3 opções:
# 1) Cadastrar Produto
# 2) Listar Produtos
# 3) Sair
import os
import time

produtos = {}

while True:
    os.system("cls")
    print("Cadastro de Produtos")
    print("-" * 20)
    print("1) Cadastrar Produto")
    print("2) Listar Produtos")
    print("3) Sair")
    opcao = int(input("Opção desejada: "))
    match opcao:
        case 1:
            os.system("cls")
            print("Cadastrar Produto")
            print("-" * 17)
            nome = input("Nome: ")
            preco = float(input("Preço: "))
            estoque = int(input("Estoque: "))
            produtos[nome] = (preco, estoque)
            print("Produto cadastrado com sucesso!")
            time.sleep(2)            
        case 2:
            os.system("cls")
            print("Listar Produtos")
            print("-" * 40)
            print(f"{'Produto':15} {'Preço':>10} {'Estoque':>10}")
            print("-" * 40)
            for nome, (preco, estoque) in produtos.items():
                print(f"{nome:15} {preco:>10.2f} {estoque:>10d}")
            print("-" * 40)
            print("Pressione ENTER para voltar ao menu...", end="")
            input()
            print("Voltando ao menu...")
            time.sleep(2)
        case 3:
            print("Saindo do sistema...")
            time.sleep(2)
            os.system("cls")  
            break          
        case _:
            print("Opção inválida. Voltando ao menu...")
            time.sleep(2)
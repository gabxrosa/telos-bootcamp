"""
##### Hands-on: Sistema de Cadastro e Análise de Usuários #####

🎯 Objetivo:

Criar um programa que permite:

✅ Cadastrar usuários com nome, idade e cidade.
✅ Listar todos os usuários cadastrados.
✅ Filtrar usuários por idade mínima.
✅ Exibir estatísticas básicas sobre os usuários.

"""

# Passo 1: Criando a Estrutura de Dados

usuarios = {}
proximo_id = 1 #ID inicial do usuário 


# Passo 2: Criando Funções para o Cadastro

    # - Função para cadastrar um usuário

def cadastrar_usuario(nome, idade, cidade):
    global proximo_id
    usuarios[proximo_id]= {"nome":nome, "idade":idade, "cidade": cidade}
    print(f"Usuário {nome} cadastrado com sucesso! ID: {proximo_id}")
    proximo_id += 1 #incrementando 1 no ID do próximo usuário
 
# Passo 3: Criando Funções para Analisar Usuários

    # - Função para listar todos os usuários
def listar_usuarios ():
    if not usuarios:
        print("Não existem usuários cadastrados!")
        return
    print("\nLista de usuários:")
    for id,dados in usuarios.items():
        print (f"ID:{id} | Nome: {dados["nome"]} | Idade: {dados["idade"]} | Cidade: {dados["cidade"]}")
       
    # - Função para filtrar usuários por idade mínima
def filtrar_por_idade(idade_minima):
    filtrados = {
        id: dados
        for id, dados in usuarios.items()
        if int(dados["idade"]) >= idade_minima
        }
    if not filtrados:
      print(f"Nenhum usuário encontrado com idade maior ou igual a {idade_minima}.")
      return
    print(f"\nUsuários com idade maior ou igual a {idade_minima}:")
    for id,dados in filtrados.items():
        print(f"ID:{id} | Nome: {dados["nome"]} | Idade: {dados["idade"]} | Cidade: {dados["cidade"]}")
    
    # - Função para exibir estatísticas gerais
def estatisticas_usuarios():
    if not usuarios:
        print("Não existem usuários cadastrados!")
        return
    total = len(usuarios)
    idades = [int(dados["idade"]) for dados in usuarios.values()]
    idade_media = sum(idades)/total
    idade_max = max(idades)
    idade_min = min(idades)

    print("\nEstatísticas dos Usuários:")
    print(f"Total de usuários: {total}")
    print(f"Idade média: {idade_media}")
    print(f"Idade máxima: {idade_max}")
    print(f"Idade mínima: {idade_min}")

# Passo 4: Criando um Menu Interativo

def menu():
    while True:
        print("\n======== MENU DO SISTEMA DE USUÁRIOS ========")
        print("1. Cadastrar um novo usuário")
        print("2. Listar todos os usuários cadastrados")
        print("3. Filtrar usuários cadastrados por idade")
        print("4. Exibir estatísticas básicas sobre usuários")
        print("5. Sair")

        opcao = input("Escolha uma opção:")

        if opcao == "1":
            nome = input("Nome:")
            idade = input("Idade:")
            cidade = input("Cidade:")
            cadastrar_usuario(nome, idade, cidade)

        elif opcao == "2":
            listar_usuarios()

        elif opcao == "3":
            idade_minima = int(input("Digite a idade mínima:"))
            filtrar_por_idade(idade_minima)

        elif opcao == "4":
            estatisticas_usuarios()

        elif opcao == "5":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida! Tente novamente.")

#Para iniciar o menu

print("=" * 45)
print("         SISTEMA DE CADASTRO DE USUÁRIOS")
print("=" * 45)
print("Bem-vindo(a) ao sistema!")
print("Você pode cadastrar usuários com nome, idade e cidade.")
print("Também pode listar, filtrar por idade e ver estatísticas.")
print("Para selecionar uma opção, digite o número correspondente.")
print("=" * 45)
menu()


        
    


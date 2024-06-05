import json

usuarios = []
livros = []

def salvar_dados():
    try:
        with open("dados.json", "w") as arquivo:
            json.dump({"usuarios": usuarios, "livros": livros}, arquivo)
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")

def carregar_dados():
    global usuarios, livros
    try:
        with open("dados.json", "r") as arquivo:
            dados = json.load(arquivo)
            usuarios = dados.get("usuarios", [])
            livros = dados.get("livros", [])
    except FileNotFoundError:
        print("Arquivo de dados não encontrado.")
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")

def menu_principal():
    carregar_dados()  
    while True:
        print("\nBem vindo! Escolha uma das opções abaixo:")
        print("1. Login")
        print("2. Gerenciar usuários")
        print("3. Cadastrar livros")
        print("4. Buscar livros")
        print("5. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            login()
        elif opcao == '2':
            menu_usuarios()
        elif opcao == '3':
            cadastrar_livros(livros)
        elif opcao == '4':
            buscar_livros()
        elif opcao == '5':
            salvar_dados()  
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

def login():
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")
    for usuario in usuarios:
        if usuario['usuario'] == nome and usuario['senha'] == senha:
            print(f"Bem-vindo, {nome}!")
            return
    print("Usuário ou senha incorretos. Tente novamente.")

def cadastrar_livros(livros):
    print("Cadastrar livros")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor do livro: ")
    ano = input("Digite o ano de publicação do livro: ")
    livros.append({'titulo': titulo, 'autor': autor, 'ano': ano})
    print(f"Livro '{titulo}' cadastrado com sucesso!")

def buscar_livros():
    print("Buscar livros")
    criterio = input("Você quer buscar por título, autor ou ano? ").lower()
    termo = input(f"Digite o {criterio} que deseja buscar: ")

    resultados = []
    for livro in livros:
        if criterio == 'título' and termo.lower() in livro['titulo'].lower():
            resultados.append(livro)
        elif criterio == 'autor' and termo.lower() in livro['autor'].lower():
            resultados.append(livro)
        elif criterio == 'ano' and termo == livro['ano']:
            resultados.append(livro)

    if resultados:
        print("Livros encontrados:")
        for livro in resultados:
            print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
    else:
        print(f"Nenhum livro encontrado para o {criterio} '{termo}'.")

def gerenciar_usuarios():
    while True:
        print("\n-------------------------------")
        print("ESCOLHA A OPÇÃO DESEJADA")
        print("1. Cadastrar usuário")
        print("2. Editar usuário")
        print("3. Excluir usuário")
        print("4. Gerar relatórios de usuários")
        print("5. Voltar ao menu principal")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            editar_usuario()
        elif opcao == '3':
            excluir_usuario()
        elif opcao == '4':
            gerar_relatorios_usuarios()
        elif opcao == '5':
            break
        else:
            print("Opção inválida, tente novamente.")

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    for usuario in usuarios:
        if usuario['usuario'] == nome:
            print("Este usuário já existe. Tente novamente.")
            return
    senha = input("Digite a senha para cadastro: ")
    usuarios.append({'usuario': nome, 'senha': senha})
    print(f"Usuário {nome} cadastrado com sucesso!")

def editar_usuario():
    nome = input("Digite o nome do usuário que deseja editar: ")
    for usuario in usuarios:
        if usuario['usuario'] == nome:
            novo_nome = input("Digite o novo nome de usuário: ")
            for u in usuarios:
                if u['usuario'] == novo_nome:
                    print("Este nome de usuário já está em uso. Tente novamente.")
                    return
            novo_senha = input("Digite a nova senha: ")
            usuario['usuario'] = novo_nome
            usuario['senha'] = novo_senha
            print("Usuário editado com sucesso.")
            return
    print("Usuário não encontrado.")

def excluir_usuario():
    nome = input("Digite o nome do usuário que deseja excluir: ")
    for usuario in usuarios:
        if usuario['usuario'] == nome:
            usuarios.remove(usuario)
            print("Usuário excluído com sucesso.")
            return
    print("Usuário não encontrado.")

def gerar_relatorios_usuarios():
    print("Lista de usuários cadastrados:")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"{i}. Nome: {usuario['usuario']}")

def menu_usuarios():
    while True:
        print("\n-------------------------------")
        print("ESCOLHA A OPÇÃO DESEJADA")
        print("1. Cadastrar usuário")
        print("2. Editar usuário")
        print("3. Excluir usuário")
        print("4. Gerar relatório de usuários")
        print("5. Voltar ao menu principal")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            editar_usuario()
        elif opcao == '3':
            excluir_usuario()
        elif opcao == '4':
            gerar_relatorios_usuarios()
        elif opcao == '5':
            break
        else:
            print("Opção inválida, tente novamente.")

menu_principal()

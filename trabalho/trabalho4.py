#Enunciado: Você e sua equipe de programadores foram contratados por pequena empresa para desenvolver o software de gerenciamento de livros. Este software deve ter o seguinte menu e opções:

#  1) Cadastrar Livro
# 2) Consultar Livro
#    1. Consultar Todos 
#   2. Consultar por Id
#  3. Consultar por Autor
# 4. Retornar ao menu
# 3) Remover Livro
# 4) Encerrar Programa







#boas vindas

print("bem vindo a livraria do Lucca Souza !")
print('-'* 90)

lista_livro = []  
id_global = 0  

# Func. cadastro livro
def cadastrar_livro(id):  
    global id_global
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")
    # atribuiçao de valores
    id = {"id": id, "nome": nome, "autor": autor, "editora": editora}
    lista_livro.append(id)
    print(f"Livro cadastrado com sucesso! ID: {id_global}")

# Func. consulta 
def consultar_livro():  
    
    while True:
        print("-------MENU CONSULTADA LIVRO-------")
        opcao = input("Consultar: 1. Todos / 2. Por Id / 3. Por Autor / 4. Retornar ao menu: ")
        #escolha do usuario
        if opcao == "1":
            for livro in lista_livro:
                print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
            #segunda escolha 
        elif opcao == "2":
            id_consulta = int(input("Digite o ID do livro: "))
            encontrado = False
            for livro in lista_livro:
                if livro["id"] == id_consulta:
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
                    encontrado = True
                    break
            if not encontrado:
                print("ID não encontrado.")
            #terceira escolha
        elif opcao == "3":
            autor_consulta = input("Digite o nome do autor: ")
            encontrados = [livro for livro in lista_livro if livro["autor"] == autor_consulta]
            if encontrados:
                for livro in encontrados:
                    print(f"ID: {livro['id']}, Nome: {livro['nome']}, Autor: {livro['autor']}, Editora: {livro['editora']}")
            else:
                print("Nenhum livro encontrado para este autor.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida")

#func. remover livro
def remover_livro():  
    while True:
        print("-------MENU REMOVE LIVRO-------")
        id_remover = int(input("Digite o ID do livro a ser removido: "))
        for livro in lista_livro:
            if livro["id"] == id_remover:
                lista_livro.remove(livro)
                print("Livro removido com sucesso!")
                return
        print("ID inválido")

# Estrutura de menu principal
while True:
    print("-----MENU PRINCIPAL-----")
    opcao = input("Menu: 1. Cadastrar Livro / 2. Consultar Livro / 3. Remover Livro / 4. Encerrar Programa: ")
    if opcao == "1":
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == "2":
        consultar_livro()
    elif opcao == "3":
        remover_livro()
    elif opcao == "4":
        print("Programa finalizado")
        break
    else:
        print("Opção inválida")

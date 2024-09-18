import os

restaurantes = [{"nome":"Burguer Queen", "categoria":"Lanchonete", "ativo":False}, 
                {"nome":"Galo Frito", "categoria":"Self-Service", "ativo":True}, 
                {"nome":"SpookBuguer", "categoria":"Lanchonete", "ativo":True}
]

def exibe_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""")

def exiber_menu():
    print("""
    [1] Cadastrar Restaurante
    [2] Listar restaurante
    [3] Alterar status do restaurante
    [4] Sair
        """)
    try:
        opcao = int(input("Escolha uma opção: "))
        
        match opcao:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                ativar_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
        

def cadastrar_novo_restaurante():
    exibir_subtitulo("CADASTRO DE RESTAURANTE")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite a categoria do restaurante {nome_restaurante}: ")
    dados_do_restaurante = {"nome":nome_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu()
    
def listar_restaurantes():
    exibir_subtitulo("LISTAGEM DE RESTAURANTE")
    cabecalho = f'{"Nome do restaurante".ljust(23)} | {"Categoria".ljust(20)} | Status'
    print(cabecalho)
    print("=" * len(cabecalho))
    
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativado" if restaurante["ativo"] else "desativado"
        print(f" - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}" ) 
    voltar_ao_menu()
    
def ativar_restaurante():
    exibir_subtitulo("ATIVAR RESTAURANTE")
    alterar_status_restaurante()
    voltar_ao_menu()
    
def finalizar_app():
    os.system("cls")
    print("Finalizando APP\n")

def opcao_invalida():
    print("Opção inválida!\n")
    voltar_ao_menu()
    
def voltar_ao_menu():
    input("\nAperte uma tecla para voltar ao menu")
    main()
    
def exibir_subtitulo(texto):
    os.system("cls")
    linha = "=" * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()
    
def alterar_status_restaurante():
    exibir_subtitulo("Alterando status do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que desejá alterar o status: ")
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")
    
def main():
    os.system("cls")
    exibe_nome_do_programa()
    exiber_menu()
    
if __name__ == '__main__':
    main()
    






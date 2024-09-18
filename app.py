import os

restaurantes = ["Burguer Queen", "Galo Frito", "SpookBuguer"]

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
    [3] Ativar restaurante
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
    restaurantes.append(nome_restaurante)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")
    voltar_ao_menu()
    
def listar_restaurantes():
    exibir_subtitulo("LISTAGEM DE RESTAURANTE")
    cont = 0
    for restaurante in restaurantes:
        cont += 1
        print(f"{cont} - {restaurante}") 
    voltar_ao_menu()
    
def ativar_restaurante():
    exibir_subtitulo("ATIVAR RESTAURANTE")
    
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
    print(f"== {texto} ==\n")
    
def main():
    os.system("cls")
    exibe_nome_do_programa()
    exiber_menu()
    
if __name__ == '__main__':
    main()
    






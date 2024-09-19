import os

from models.restaurante import Restaurante, ativar_restaurante, cadastrar_novo_restaurante, listar_restaurantes

restaurante1 = Restaurante("Burguer Queen", "Lanchonete")
restaurante2 = Restaurante("Galo Frito", "Self-Service")
restaurante3 = Restaurante("SpookBuguer", "Lanchonete")

Restaurante.restaurantes = [restaurante1, restaurante2, restaurante3]

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
                voltar_ao_menu()
            case 2:
                listar_restaurantes()
                voltar_ao_menu()
            case 3:
                ativar_restaurante()
                voltar_ao_menu()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
        
def finalizar_app():
    os.system("cls")
    print("Finalizando APP\n")

def opcao_invalida():
    print("Opção inválida!\n")
    voltar_ao_menu()

def voltar_ao_menu():
    input("\nAperte uma tecla para voltar ao menu")
    main()
   
def main():
    os.system("cls")
    exibe_nome_do_programa()
    exiber_menu()
    
if __name__ == '__main__':
    main()
    
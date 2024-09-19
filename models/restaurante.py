import os

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return self.nome

def cadastrar_novo_restaurante():
    exibir_subtitulo("CADASTRO DE RESTAURANTE")
    nome_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
    categoria = input(f"Digite a categoria do restaurante {nome_restaurante}: ")
    novo_restaurante = Restaurante(nome_restaurante, categoria)
    print(f"O restaurante {nome_restaurante} foi cadastrado com sucesso!")


def listar_restaurantes():
    exibir_subtitulo("LISTAGEM DE RESTAURANTE")
    cabecalho = f'{"Nome do restaurante".ljust(23)} | {"Categoria".ljust(20)} | Status'
    print(cabecalho)
    print("=" * len(cabecalho))
    for restaurante in Restaurante.restaurantes:
        nome_restaurante = restaurante.nome
        categoria = restaurante.categoria
        ativo = "ativado" if restaurante.ativo == True else "desativado"
        print(f" - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}" ) 


def ativar_restaurante():
    exibir_subtitulo("ATIVAR RESTAURANTE")
    alterar_status_restaurante()


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

    for restaurante in Restaurante.restaurantes:
        if nome_restaurante == restaurante.nome:
            restaurante_encontrado = True
            restaurante.ativo = not restaurante.ativo
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante.ativo == True else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")

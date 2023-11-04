import os
from bd import BD
# Classe para interface do usuário do programa

class Interface:
    # Construtor
    def __init__(self):
        self.banco = BD("catalogoAnimais.db")

    def logotipo(self):
        print()
        print("=============================")
        print("=====Catalogo de Animais=====")
        print("=============================")
        print()

    def limpaTela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Função que permite o usuário escolher uma opção
    # opcoes = []
    def selecionaOpcao(self, opcoesPermitidas = []):
        opcaoSelecionada = input("Digite a opção desejada: ")

        # Verifica se digitou algo
        if opcaoSelecionada == "":
            return self.selecionaOpcao(opcoesPermitidas)

        # Tenta converter para números
        try:
            opcaoSelecionada = int(opcaoSelecionada)
        except ValueError:
            print("Opção Inválida!")
            return self.selecionaOpcao(opcoesPermitidas)

        # Verifica se a opção selecionada é uma das opções válidas
        if opcaoSelecionada not in opcoesPermitidas:
            print("Opção Inválida!")
            return self.selecionaOpcao(opcoesPermitidas)

        # Retorna o valor selecionado pelo usuário
        return opcaoSelecionada

    # Mostra menu principal do sistema
    def mostraMenuPrincipal(self):
        print("1 - Cadastrar Animais")
        print("2 - Lista de Animais")
        print("0 - Sair")
        print()

    def mostraCadastroAnimais(self):
        self.logotipo()

        print("Insira os dados do Animal:")
        print("(campos com * são obrigatórios)")
        print()

        nome = self.solicitaValor('Digite o nome*: ', 'texto', False)
        raca = self.solicitaValor('Digite a raça*: ', 'texto', False)
        tamanho = self.solicitaValor('Digite o tamanho: ', 'texto', True)
        idade = self.solicitaValor('Digite a idade: ', 'numero', True)

        # Armazena os valores no banco de dados!
        valores = {
            "nome": nome,
            "raca": raca,
            "tamanho": tamanho,
            "idade": idade
        }

        self.banco.inserir('Animais', valores)

    def mostrarListaAnimais(self):
        self.logotipo()
        print("Veja abaixo a lista de animais cadastrados.")
        print()
        print("ID - Nome - Raça - Tamanho - Idade")
        animais = self.banco.buscaDados('Animais')

        for animal in animais:
            id, nome, raca, tamanho, idade = animal

            print(f"{id} - {nome} - {raca} - {tamanho} - {idade}")

        print()

        input("Aperte Enter para continuar...")

    # Solicita um valor do usuário e valida ele.
    # return valorDigitado
    def solicitaValor(self, legenda, tipo = 'texto', permiteNulo = False):
        valor = input(legenda)

        # Verifica se está vazio
        if valor == "" and not permiteNulo:
            print("Valor inválido!")
            return self.solicitaValor(legenda, tipo, permiteNulo)
        elif valor == "" and permiteNulo:
            return valor
        
        # Verifica se está no formato correto
        if tipo == 'numero':
            try:
                valor = float(valor)
            except ValueError:
                print("Valor Inválido!")
                return self.solicitaValor(legenda, tipo, permiteNulo)
            
        return valor
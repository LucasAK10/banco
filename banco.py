# código para funcionamento do módulo
import datetime

class Banco:
    def __init__(self):
        self.usuarios = {}

    def menu_principal(self):
        print("Bem-vindo ao Banco Python!")
        print("1. Entrar")
        print("2. Cadastrar")
        print("3. Deletar")
        print("4. Sair")

    def menu_usuario(self):
        print("Menu do Usuário:")
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Sair")

    def cadastrar_usuario(self):
        nome = input("Digite seu nome: ")
        if nome not in self.usuarios:
            self.usuarios[nome] = Conta(nome)
            print("Usuário cadastrado com sucesso!")
        else:
            print("Usuário já cadastrado!")

    def deletar_usuario(self):
        nome = input("Digite seu nome: ")
        if nome in self.usuarios:
            del self.usuarios[nome]
            print("Usuário deletado com sucesso!")
        else:
            print("Usuário não encontrado!")

    def entrar(self):
        nome = input("Digite seu nome: ")
        if nome in self.usuarios:
            return self.usuarios[nome]
        else:
            print("Usuário não encontrado!")
            return None

class Conta:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0.0
        self.data_consulta = None

    def consultar_saldo(self):
        self.data_consulta = datetime.datetime.now()
        return self.saldo, self.data_consulta

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False
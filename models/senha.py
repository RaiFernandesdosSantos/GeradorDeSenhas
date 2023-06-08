import secrets
import string
import re

from models.conexao import Conexao


class Senha:
    def __init__(self):
        self.conexao = Conexao()
        self.pontuacao = 0
        self.senha = []

        if self.conexao is not None:
            print("Sucesso")
        else:
            print("Erro")

    # Region: Password Generation

    def gerarSenha(self, length):
        itens = string.ascii_letters + string.digits + "!@#$&*?<>"

        # Add one character from each category
        self.senha.append(secrets.choice(string.ascii_uppercase))
        self.senha.append(secrets.choice(string.ascii_lowercase))
        self.senha.append(secrets.choice(string.digits))
        self.senha.append(secrets.choice("!@#$&*?<>"))

        # Add remaining characters randomly
        for i in range(length - 4):
            self.senha.append(secrets.choice(itens))

        # Shuffle the password and join it into a string
        secrets.SystemRandom().shuffle(self.senha)
        self.senha = "".join(self.senha)

    # Region: Getters and Setters

    def getSenha(self):
        return str(self.senha)

    # Region: Password Management

    def listarSenha(self):
        sql = "SELECT * FROM senha"

        try:
            rs = self.conexao.executeSql(sql)

            senhas = []

            for row in rs:
                entrada = list(row)
                senhas.append(entrada)

            print(senhas)
            return senhas

        except Exception as e:
            print(f"Erro: {str(e)}")
            return []

    def guardarSenha(self, descricao, senha):
        sql = "INSERT INTO senha (descricao, senha) VALUES (?, ?)"

        try:
            self.conexao.executeSql(sql, (descricao, senha))
        except Exception as e:
            print(f"Erro {str(e)}")

    def editaSenha(self, descricao, senha):
        pass

    def deleteSenha(self, id):
        pass

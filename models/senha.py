import secrets
import string
from conexao import Conexao


class Senha:
    def __init__(self, lenght):
        self.length = lenght
        self.itens = string.ascii_letters + string.digits + "!@#$&*?<>"
        self.conexao = Conexao()

    # Region: Password Generation

    def gerarSenha(self):
        senha = []

        # Add one character from each category

        senha.append(secrets.choice(string.ascii_uppercase))
        senha.append(secrets.choice(string.ascii_lowercase))
        senha.append(secrets.choice(string.digits))
        senha.append(secrets.choice("!@#$&*?<>"))

        # Add remaining characters randomly

        for i in range(self.length - 4):
            senha.append(secrets.choice(self.itens))

        # Shuffle the password and join it into a string

        secrets.SystemRandom().shuffle(senha)
        senha = "".join(senha)

        return senha

    # Region: Password Management

    def guardarSenha(self, descricao, senha):
        pass

    def editaSenha(self, descricao, senha):
        pass

    def deleteSenha(selfa, id):
        pass

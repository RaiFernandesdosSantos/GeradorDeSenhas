import secrets
import string


class Senha:
    def __init__(self, lenght):
        self.length = lenght
        self.itens = string.ascii_letters + string.digits + "!@#$&*?<>"

    def gerarSenha(self):
        senha = []

        senha.append(secrets.choice(string.ascii_uppercase))
        senha.append(secrets.choice(string.ascii_lowercase))
        senha.append(secrets.choice(string.digits))
        senha.append(secrets.choice("!@#$&*?<>"))

        for i in range(self.length - 4):
            senha.append(secrets.choice(self.itens))

        secrets.SystemRandom().shuffle(senha)
        senha = "".join(senha)

        return senha

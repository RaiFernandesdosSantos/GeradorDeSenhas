import secrets
import string
import re

from models.conexao import Conexao


class Senha:
    def __init__(self):
        self.conexao = Conexao()
        self.pontuacao = 0
        self.senha = []
        self.senhaString = ""

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
        self.senhaString = "".join(self.senha)

    # Region: Password Strength Test

    def testarSenha(self, senha, length, senhaString, especial):
        caracterRepetido = 0
        meioSenha = senhaString[1:-1]
        requerimentos = 0
        soLetra = 0
        soNumero = 0

        # Cehck if has any repeated character
        for i in range(len(senha)):
            for j in range(i + 1, len(senha)):
                if senha[i] == senha[j]:
                    caracterRepetido += 1

        maiuscula = sum(char.isupper() for char in senhaString)
        minuscula = sum(char.islower() for char in senhaString)
        numero = sum(char.isnumeric() for char in senhaString)
        outros = sum(char in especial for char in senhaString)
        numeroMeio = sum(char.isnumeric() for char in meioSenha)
        simboloMeio = sum(char in especial for char in meioSenha)

        # Check the requirements of the password
        if len(senhaString) >= 8:
            requerimentos += 1
        if maiuscula >= 1:
            requerimentos += 1
        if minuscula >= 1:
            requerimentos += 1
        if numero >= 1:
            requerimentos += 1
        if outros >= 1:
            requerimentos += 1

        if (maiuscula + minuscula) == len(senhaString):
            soLetra = len(senhaString)

        if numero == len(senhaString):
            soNumero = len(senhaString)

        minusculaConsecutiva = max(
            len(match.group()) for match in re.finditer(r"[a-z]+", senhaString)
        )
        maiusculaConsecutiva = max(
            len(match.group()) for match in re.finditer(r"[A-Z]+", senha)
        )
        numeroConsecutivo = max(
            len(match.group()) for match in re.finditer(r"\d+", senha)
        )

        sequenciaLetras = self.contaSequencia(senhaString)
        sequenciaNumeros = self.contaSequencia(senhaString)

        # Formule to the pontuation system
        self.pontuacao = (
            (length * 4)
            + ((len(senhaString) - maiuscula) * 2)
            + ((len(senhaString) - minuscula) * 2)
            + (numero * 4)
            + (outros * 6)
            + ((numeroMeio + simboloMeio) * 2)
            + requerimentos
        ) - (
            soLetra
            + soNumero
            + (caracterRepetido * (caracterRepetido - 1))
            + (maiusculaConsecutiva * 2)
            + (minusculaConsecutiva * 2)
            + (numeroConsecutivo * 2)
            + (sequenciaLetras * 3)
            + (sequenciaNumeros * 3)
        )

        print(self.pontuacao)

    def contaSequencia(self, senha):
        count = 0

        for i in range(len(senha) - 2):
            sequence = senha[i : i + 3]
            if sequence.isalpha() and sequence.islower():
                if sequence in string.ascii_lowercase:
                    count += 1
            elif sequence.isalpha() and sequence.isupper():
                if sequence in string.ascii_uppercase:
                    count += 1
            elif sequence.isdigit():
                if sequence in string.digits:
                    count += 1

        return count

    # Region: Getters and Setters

    def getSenha(self):
        return str(self.senhaString)

    # Region: Password Management

    def listarSenha(self):
        sql = "SELECT * FROM gerenciadorSenha"

        try:
            rs = self.conexao.executeSql(sql)
            dicionario = [dict(row) for row in rs]
            return dicionario

        except Exception as e:
            print(f"Erro: {str(e)}")
            return []

    def guardarSenha(self, descricao, senha, lenght):
        sql = "INSERT INTO gerenciadorSenha (descricao, senha, pontuacao) VALUES (?, ?, ?)"

        self.testarSenha(self.senha, lenght, self.senhaString, "!@#$&*?<>")

        try:
            self.conexao.executeSql(sql, (descricao, senha, self.pontuacao))
        except Exception as e:
            print(f"Erro {str(e)}")

    def editaSenha(self, descricao, senha):
        pass

    def deleteSenha(self, id):
        pass

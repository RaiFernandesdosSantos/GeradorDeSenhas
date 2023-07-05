import random
import string

from models.conexao import Conexao


class Senha:
    def __init__(self):
        self.conexao = Conexao()
        self.pontuacao = 0

        if self.conexao is not None:
            print("Sucesso")
        else:
            print("Erro")

    # Region: Password Generation

    def gerarSenha(self, length):
        """
        Generate a random password of the specified length.

        Args:
            length (int): The length of the password.

        Returns:
            None
        """
        # Define the characters that can be included in the password
        itens = string.ascii_letters + string.digits + "!@#$&*?<>"

        # Initialize an empty list to store the password characters
        self.senha = []

        # Add one character from each category
        self.senha.extend(random.choice(string.ascii_uppercase))
        self.senha.extend(random.choice(string.ascii_lowercase))
        self.senha.extend(random.choice(string.digits))
        self.senha.extend(random.choice("!@#$&*?<>"))

        # Add remaining characters randomly
        for _ in range(length - 8):
            self.senha.append(random.choice(itens))

        # Shuffle the password and join it into a string
        random.shuffle(self.senha)

        # Join the password characters into a string
        self.senha = "".join(self.senha)

    # Region: Getters and Setters

    def get_senha(self):
        """
        Returns the senha attribute as a string.
        """
        return str(self.senha)

    # Region: Password Management

    def listarSenha(self):
        """
        Retrieve all the rows from the 'senha' table.

        Returns:
            A list of lists representing the rows from the 'senha' table.
            Each inner list contains the values of a single row.
        """
        sql = "SELECT * FROM senha"

        try:
            rs = self.conexao.executeSql(sql)
            senhas = [list(row) for row in rs]
            return senhas

        except Exception as e:
            print(f"Erro: {str(e)}")
            return []

    def guardarSenha(self, descricao, senha):
        """
        Saves a password with its description to the database.

        Args:
            descricao (str): The description of the password.
            senha (str): The password to be saved.

        Returns:
            None
        """
        sql = "INSERT INTO senha (descricao, senha) VALUES (?, ?)"
        self.conexao.executeSql(sql, (descricao, senha))

    def editaSenha(self, descricao, senha):
        pass

    def deleteSenha(self, id):
        pass

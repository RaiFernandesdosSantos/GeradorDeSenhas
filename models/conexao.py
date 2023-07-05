import sqlite3


class Conexao:
    def __init__(self):
        self.conectar()

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS senha (id INTEGER PRIMARY KEY AUTOINCREMENT, descricao TEXT NOT NULL, senha TEXT NOT NULL, pontuacao INTEGER NOT NULL)"
        )

        self.conexao.commit()
        self.desconectar()

    # Region: Connection Management

    def desconectar(self):
        """
        Disconnects from the database by closing the cursor and the connection.
        """
        self.cursor.close()
        self.conexao.close()

    def conectar(self):
        # Database connection setup
        self.conexao = sqlite3.connect("gerenciadorSenha.db")

        self.cursor = self.conexao.cursor()

        if self.conexao is not None:
            print("Sucesso")
        else:
            print("Erro")

    # Region: Query Execution

    def executeSql(self, sql, params=None):
        """
        Executes the given SQL query and returns the result set if it's a SELECT query.
        If the query is not a SELECT query, it commits the changes to the database.

        Args:
            sql (str): The SQL query to execute.
            params (tuple, optional): The parameters to substitute in the query.

        Returns:
            list: The result set if the query is a SELECT query, otherwise an empty list.
        """
        self.conectar()
        rs = []

        try:
            if params is not None:
                self.cursor.execute(sql, params)
            else:
                self.cursor.execute(sql)

            if not sql.strip().lower().startswith("select"):
                self.conexao.commit()
            else:
                rs = self.cursor.fetchall()

        except Exception as e:
            print(f"Erro: {str(e)}")

        self.desconectar()

        return rs

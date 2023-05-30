import sqlite3


class Conexao:
    def __init__(self):
        self.conectar()

        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS senha (id INTEGER PRIMARY KEY AUTOINCREMENT, descricao TEXT NOT NULL, senha TEXT NOT NULL)"
        )

        self.conexao.commit()
        self.desconectar()

    # Region: Connection Management

    def desconectar(self):
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

    def executeSql(self, sql):
        self.conectar()
        rs = []

        # Execute the query

        self.cursor.execute(sql)

        if not sql.strip().lower().startswith("select"):
            # For non-SELECT queries, commit the changes to the database
            self.conexao.commit()
        else:
            # For SELECT queries, fetch the result set
            rs = self.cursor.fetchall()

        self.desconectar()

        return rs


conn = Conexao()

import mysql.connector


class Conexao:
    def __init__(self):
        self.conectar()

    # Region: Connection Management

    def desconectar(self):
        self.cursor.close()
        self.conexao.close()

    def conectar(self):
        # Database connection setup
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="10253565#Rai",
            database="senha",
        )

        self.cursor = self.conexao.cursor()

        if self.conexao.is_connected():
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

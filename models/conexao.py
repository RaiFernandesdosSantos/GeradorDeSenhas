import mysql.connector

conexao = mysql.connector.connect(
    host="localhost", user="root", password="10253565#Rai", database="senha"
)

cursor = conexao.cursor()

cursor.close()
conexao.close()

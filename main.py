import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from models.senha import Senha


def geraSenha():
    tamanho = int(home.tamanhoSenha.text())
    senha = Senha(tamanho)
    password = str(senha.gerarSenha())

    home.senhaGerada.setText(password)


path = os.path.dirname(__file__)
homeFile = os.path.join(path, "view", "home.ui")

app = QApplication(sys.argv)
home = uic.loadUi(homeFile)

home.gerarSenha.clicked.connect(lambda: geraSenha())

home.show()
app.exec()

from PyQt6.QtCore import QObject, pyqtSlot, QVariant
from models.senha import Senha


class ProcessaFormulario(QObject):
    @pyqtSlot(int, result=QVariant)
    def generateSenha(self, lenght):
        senha = Senha(lenght)
        senha.gerarSenha()

        return QVariant(senha.getSenha())

    @pyqtSlot(str, str)
    def guardaSenha(self, senha, descricao):
        password = Senha(0)
        password.guardarSenha(descricao, senha)

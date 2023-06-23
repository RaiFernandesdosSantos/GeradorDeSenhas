from PyQt6.QtCore import QObject, pyqtSlot, QVariant
from models.senha import Senha


class ProcessaFormulario(QObject):
    @pyqtSlot(int, result=QVariant)
    def generateSenha(self, lenght):
        senha = Senha()
        senha.gerarSenha(lenght)
        return QVariant(senha.getSenha())

    @pyqtSlot(str, str)
    def guardaSenha(self, senha, descricao):
        password = Senha()
        password.guardarSenha(descricao, senha)

    @pyqtSlot(result=QVariant)
    def listaSenhas(self):
        senha = Senha()
        listaSenha = senha.listarSenha()
        return QVariant(listaSenha)

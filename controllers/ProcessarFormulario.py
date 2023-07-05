from PyQt6.QtCore import QObject, pyqtSlot, QVariant
from models.senha import Senha


class ProcessaFormulario(QObject):
    @pyqtSlot(int, result=QVariant)
    def generateSenha(self, length):
        """
        Generates a password of the specified length.

        Args:
            length (int): The length of the password to be generated.

        Returns:
            QVariant: The generated password as a QVariant object.
        """
        return QVariant(Senha().gerarSenha(length))

    @pyqtSlot(str, str)
    def guarda_senha(self, senha: str, descricao: str) -> None:
        """
        Guarda a senha informada.

        Args:
            senha (str): A senha a ser guardada.
            descricao (str): A descrição da senha.

        Returns:
            None
        """
        Senha().guardarSenha(descricao, senha)

    @pyqtSlot(result=QVariant)
    def listaSenhas(self):
        """
        A function that returns a list of passwords.

        Returns:
            QVariant: A QVariant object containing the list of passwords.
        """
        senha = Senha()
        return QVariant(senha.listarSenha())

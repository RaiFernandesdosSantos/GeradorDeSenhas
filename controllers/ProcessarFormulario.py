from PyQt6.QtCore import QObject, pyqtSlot


class ProcessaFormulario(QObject):
    @pyqtSlot(int)
    def generateSenha(self, lenght):
        print(f"Lenght recebida {lenght}")

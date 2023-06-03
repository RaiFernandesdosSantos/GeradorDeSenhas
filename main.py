from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import sys
import os
from controllers.ProcessarFormulario import ProcessaFormulario
from PyQt6.QtWebChannel import QWebChannel

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Gerador de senhas")
window.resize(700, 550)

view = QWebEngineView(window)

path = os.path.dirname(__file__)
home = os.path.join(path, "view", "home", "index.html")

view.setUrl(QUrl.fromLocalFile(home))

processarForm = ProcessaFormulario()
webChannel = QWebChannel(view.page())
webChannel.registerObject("processaFormulario", processarForm)
view.page().setWebChannel(webChannel)

window.setCentralWidget(view)
window.show()
sys.exit(app.exec())

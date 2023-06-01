from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
import sys
import os

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Gerador de senhas")
window.resize(700, 550)

view = QWebEngineView(window)

path = os.path.dirname(__file__)
home = os.path.join(path, "view", "home", "index.html")

view.setUrl(QUrl.fromLocalFile(home))

window.setCentralWidget(view)
window.show()
sys.exit(app.exec())

from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
import sys

app = QApplication(sys.argv)
view = QWebEngineView()
view.load(QUrl("https://google.com"))
view.show()
sys.exit(app.exec())

from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QMainWindow


class Mapping(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(1000, 200, 1000, 1000)
        self.mapp = QWebEngineView(self)
        self.mapp.setUrl(QUrl('https://maps.google.com'))
        self.mapp.resize(1000, 1000)
        self.mapp.move(0, 0)


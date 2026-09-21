import sys
import requests
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
)
from PyQt5.QtCore import Qt

base_url = "https://api.openweathermap.org/data/2.5/weather?q="
api_key = ""


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My weather app")
        self.setGeometry(700, 200, 500, 500)

        self.initUI()


def main():
    app = QApplication(sys.argv)
    window = MainWindow
    window.show()
    sys.ecit(app.exec_())


if __name__ == "__main__":
    main()

import requests
import sys
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QMainWindow,
    QScrollArea,
)

import json

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nasa Api")
        self.setGeometry(700, 200, 500, 500)

        self.initUI()
        self.fetch_apod()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.TitleLabel = QLabel("NASA DASHBOARD")
        self.TitleLabel.setStyleSheet("font-size:30px; font-family: Arial;")

        self.NameLabel = QLabel("")
        self.NameLabel.setStyleSheet("font-size:20px; font-family: Arial;")

        self.DateLabel = QLabel("")
        self.DateLabel.setStyleSheet("font-size:20px; font-family: Arial;")

        self.ImageLabel = QLabel()

        self.pixmap = QPixmap()
        self.ImageLabel.setPixmap(self.pixmap)

        self.ExplanationLabel = QLabel("")
        self.ExplanationLabel.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.ExplanationLabel.setWordWrap(True)
        self.ExplanationLabel.setTextFormat(Qt.RichText)
        self.ExplanationLabel.setOpenExternalLinks(True)

        vbox = QVBoxLayout()
        vbox.addWidget(self.TitleLabel)
        vbox.addWidget(self.NameLabel)
        vbox.addWidget(self.DateLabel)
        vbox.addWidget(self.ImageLabel)
        vbox.addWidget(self.ExplanationLabel)

        central_widget.setLayout(vbox)
        scroll = QScrollArea()
        scroll.setWidget(central_widget)
        scroll.setWidgetResizable(True)

        self.setCentralWidget(scroll)

    # APOD is referring to Astheroid Picture of the Day
    def fetch_apod(self):

        api_key = ""
        apod_url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic/"

        url = f"{apod_url}?api_key={api_key}"

        try:
            res = requests.get(url)

            data = res.json()
            print(json.dumps(data[0], indent=4))
            print(data[0]["title"])
            print(data[0]["date"])
            print(data[0]["hdurl"])
            self.NameLabel.setText(data[0]["title"])
            self.DateLabel.setText(data[0]["date"])
            self.ExplanationLabel.setText(data[0]["explanation"])

            image_res = requests.get(data[0]["hdurl"])
            self.pixmap.loadFromData(image_res.content)
            scaled_pixmap = self.pixmap.scaled(
                450, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.ImageLabel.setPixmap(scaled_pixmap)

        except requests.RequestException as e:
            print(f"Error when fetching the data: {e}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

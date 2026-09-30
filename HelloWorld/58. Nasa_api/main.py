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
    QPushButton,
    QLineEdit,
)

import json

from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from datetime import datetime, timedelta


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

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Insert the date")
        self.line_edit.setStyleSheet("font-size: 30px; border-radius: 15px;")

        self.search_button = QPushButton("Search")
        self.search_button.setStyleSheet(
            "font-size: 15px; font-family: Arial; color: white; background-color: black;"
        )
        self.search_button.clicked.connect(self.fetch_from_search)

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

        self.next_button = QPushButton("Next➡️")
        self.next_button.setStyleSheet(
            "font-size: 15px; font-family: Arial; background-color: #a4a6a6; color: white;"
        )
        self.next_button.clicked.connect(self.fetch_next)

        self.previous_button = QPushButton("⬅️Previous")
        self.previous_button.setStyleSheet(
            "font-size: 15px; font-family: Arial; background-color: #a4a6a6; color: white;"
        )
        self.previous_button.clicked.connect(self.fetch_previous)

        hbox = QHBoxLayout()
        hbox.addWidget(self.previous_button)
        hbox.addWidget(self.next_button)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.line_edit)
        hbox2.addWidget(self.search_button)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
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
    def fetch_apod(self, date=None):

        if date is None:
            date = datetime.today().strftime("%Y-%m-%d")

        nasa_date = datetime.strptime(date, "%Y-%m-%d").strftime("%y%m%d")

        self.apod_url = f"https://science.nasa.gov/wp-json/wp/v2/apod-basic/{nasa_date}"

        try:
            res = requests.get(self.apod_url)

            data = res.json()

            print("STATUS:", res.status_code)
            print("URL:", res.url)
            print("RESPONSE:", res.text[:1000])

            print(json.dumps(data, indent=4))
            print(data["title"])
            print(data["date"])
            print(data["hdurl"])
            self.NameLabel.setText(data["title"])
            self.DateLabel.setText(data["date"])
            self.ExplanationLabel.setText(data["explanation"])

            self.current_date = datetime.strptime(data["date"], "%Y-%m-%d")
            print(self.current_date)

            image_res = requests.get(data["hdurl"])
            self.pixmap.loadFromData(image_res.content)
            scaled_pixmap = self.pixmap.scaled(
                450, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            self.ImageLabel.setPixmap(scaled_pixmap)

        except requests.RequestException as e:
            print(f"Error when fetching the data: {e}")

    def fetch_next(self):

        next_date = self.current_date + timedelta(days=1)

        self.now = datetime.today()

        if next_date > self.now:
            print("Hey, don't think about tomorrow, think about today!")
            return

        self.fetch_apod(next_date.strftime("%Y-%m-%d"))

        print(self.current_date)

    def fetch_previous(self):

        previous_date = self.current_date - timedelta(days=1)

        self.fetch_apod(previous_date.strftime("%Y-%m-%d"))

        print(previous_date)

    def fetch_from_search(self):
        print("gasi")

        date_from_search = self.line_edit.text()

        self.fetch_apod(date_from_search)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

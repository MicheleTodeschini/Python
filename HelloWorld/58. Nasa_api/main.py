import requests
import sys
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QMainWindow,
)


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

        self.DateLabel = QLabel()
        self.DateLabel.setStyleSheet("font-size:20px; font-family: Arial;")

        vbox = QVBoxLayout()
        vbox.addWidget(self.TitleLabel)
        vbox.addWidget(self.NameLabel)
        vbox.addWidget(self.DateLabel)

        central_widget.setLayout(vbox)

    # APOD is referring to Astheroid Picture of the Day
    def fetch_apod(self):

        api_key = ""
        apod_url = "https://science.nasa.gov/wp-json/wp/v2/apod-basic/"

        url = f"{apod_url}?api_key={api_key}"

        try:
            res = requests.get(url)

            data = res.json()
            print(data[0]["title"])
            print(data[0]["date"])
            self.NameLabel.setText(data[0]["title"])
            self.DateLabel.setText(data[0]["date"])
        except:
            print(f"Error when fetching the data {res.status_code}")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

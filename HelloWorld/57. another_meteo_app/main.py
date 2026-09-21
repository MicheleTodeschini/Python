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
    QWidget,
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

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Type the city here")
        self.line_edit.setStyleSheet("font-size: 30px; border-radius: 15px;")

        self.button = QPushButton("Search")
        self.button.setStyleSheet(
            "font-size: 20px; font-family: Arial; background-color: #3db6f2; color: white;"
        )
        self.button.clicked.connect(self.submit)

        self.labelUp = QLabel("")
        self.labelCenter = QLabel("")
        self.labelDown = QLabel("")
        self.labelUp.setStyleSheet("font-size: 50px;")
        self.labelCenter.setStyleSheet("font-size: 50px;")
        self.labelDown.setStyleSheet("font-size: 50px;")
        self.labelUp.setAlignment(Qt.AlignCenter)
        self.labelCenter.setAlignment(Qt.AlignCenter)
        self.labelDown.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.line_edit)
        hbox.addWidget(self.button)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.labelUp)
        vbox.addWidget(self.labelCenter)
        vbox.addWidget(self.labelDown)

        central_widget.setLayout(vbox)

    def submit(self):
        print("pressed")
        text = self.line_edit.text()

        try:

            url = f"{base_url}{text}&appid={api_key}&units=metric"
            res = requests.get(url)
            if res.status_code == 200:
                data = res.json()
                print(data)
                weather = data["weather"][0]["main"]
                temperature = data["main"]["temp"]

                if weather == "Thunderstorm":
                    self.labelCenter.setText("⛈️")
                elif weather == "Clear":
                    self.labelCenter.setText("☀️")
                elif weather == "Rain":
                    self.labelCenter.setText("🌧️")
                elif weather == "Clouds":
                    self.labelCenter.setText("☁️")

                self.labelUp.setText(f"{text}")
                self.labelDown.setText(f"{temperature:.1f} °C")

                self.line_edit.settext("")

            else:
                print(f"Failed to retrieve data {res.status_code}")

        except:
            print("Can't reach the Api. Check if the wifi is active")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

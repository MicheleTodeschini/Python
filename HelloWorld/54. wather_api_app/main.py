#PyQt5 Weather Api App

import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
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
        # ALL REGARDING THE INPUT 
        self.line_edit = QLineEdit()
        self.line_edit.setStyleSheet("font-size: 30px;")
        self.line_edit.setPlaceholderText("Type the city")
         # ALL REGARDING THE BUTTON 
        self.button = QPushButton("Search")
        self.button.setStyleSheet( "font-size: 20px; font-family: Arial;" )
        # ALL REGARDING LINE EDIT
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.line_edit.setStyleSheet("font-size: 30px;")
        self.line_edit.setPlaceholderText("Type the city")
        # ALL REGARDING THR BUTTON
        self.button.setGeometry(210, 10, 100, 40)
        self.button.setStyleSheet("font-size: 20px; font-family: Arial;")
        self.button.clicked.connect(self.submit_and_get_info)
        # ALL REGARDING THE LABELS
        self.labelTop = QLabel("top")
        self.labelCenter = QLabel("center")
        self.labelBottom = QLabel("bottom")
        self.labelTop.setStyleSheet("font-size: 50px;")
        self.labelCenter.setStyleSheet("font-size: 50px;")
        self.labelBottom.setStyleSheet("font-size: 50px;")
        self.labelTop.setAlignment(Qt.AlignCenter)
        self.labelCenter.setAlignment(Qt.AlignCenter)
        self.labelBottom.setAlignment(Qt.AlignCenter)


        # ALL REGARDING THE LAYOUT
        hbox = QHBoxLayout()
        hbox.addWidget(self.line_edit)
        hbox.addWidget(self.button)
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.labelTop)
        vbox.addWidget(self.labelCenter)
        vbox.addWidget(self.labelBottom)

        central_widget.setLayout(vbox)


    def submit_and_get_info(self):
        print("tasto premuto")
        text = self.line_edit.text()
        url = f"{base_url}{text}&appid={api_key}"

        res = requests.get(url)

        if res.status_code == 200:

            weather_data = res.json()

            print(weather_data)
            

        weather = weather_data["weather"][0]["main"]
        
        if weather == "Thunderstorm":
            self.labelTop.setText("⛈️")

        elif weather == "Drizzle":
            self.labelTop.setText("🌦️")

        elif weather == "Rain":
            self.labelTop.setText("🌧️")

        elif weather == "Snow":
            self.labelTop.setText("❄️")

        elif weather == "Clear":
            self.labelTop.setText("☀️")

        elif weather == "Clouds":
            self.labelTop.setText("☁️")
            return weather  
        else:
            print(f"Failed to retrieve data {res.status_code}")



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
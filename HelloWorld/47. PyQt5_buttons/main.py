#PyQt5 buttons

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first python GUI")
        self.setGeometry(700, 200, 500, 500)
        self.initUI()

    def initUI(self):
        self.button = QPushButton("Click me!", self) 
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click) 

    def on_click(self):
        print("Button clicked!")
        self.button.setText("Clicked!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
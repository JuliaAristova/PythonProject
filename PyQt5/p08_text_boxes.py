# PyQt5 - Line edits = text boxes

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(750, 350, 500, 500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(20, 20, 200, 40)
        self.line_edit.setStyleSheet("font-size: 20px;"
                                     "font_family: Arial")
        self.line_edit.setPlaceholderText("Enter your name")

        self.button.setGeometry(230, 20, 100, 40)
        self.button.setStyleSheet("font-size: 20px;"
                                "font_family: Arial;")


        self.button.clicked.connect(self.submit)


    def submit(self):
        #print("You clicked the button!")
        text = self.line_edit.text()
        print(f"Hello, {text}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
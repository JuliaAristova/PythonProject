# PyQt5 introduction

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first GUI")
        self.setGeometry(750, 400, 500, 500)   # initial placement x, y, width, height
        self.setWindowIcon(QIcon("Dog.png"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()               #default behavior - to hide
    window.show()                       # to see the window
    sys.exit(app.exec_())               # execute method

if __name__ == "__main__":
    main()

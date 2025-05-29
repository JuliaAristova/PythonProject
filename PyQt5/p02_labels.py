# PyQt5 QLabels

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont                   # for fonts
from PyQt5.QtCore import Qt                     # for alighnments

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(750, 400, 500, 500)

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline")
       # label.setAlignment(Qt.AlignTop)                 # alight vertically to the top
       # label.setAlignment(Qt.AlignBottom)
       # label.setAlignment(Qt.AlignVCenter)
       # label.setAlignment(Qt.AlignRight)                # align horizontally to the right
       # label.setAlignment(Qt.AlignHCenter)
       # label.setAlignment(Qt.AlignLeft)
       # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        label.setAlignment(Qt.AlignCenter)                # shortcut for above

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


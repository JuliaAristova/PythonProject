# PyQt5 Images

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap                             # to work with images

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(750, 400, 500, 500)

        label = QLabel(self)
        label.setGeometry(0, 0, 100, 100)  # position x, y, width, height

        #pixmap = QPixmap("nature.jpg")
        pixmap = QPixmap("dog.png")
        label.setPixmap(pixmap)

        label.setScaledContents(True)       # to scale image
        #label.setGeometry(0, 0, label.width(), label.height())
        '''
        label.setGeometry(self.width() - label.width(),  # right bottom corner
                          self.height() - label.height(),
                          label.width(),
                          label.height())
        '''
        # set in the center
        label.setGeometry((self.width() - label.width())//2,
                          (self.height() - label.height())//2,
                            label.width(),
                            label.height())


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
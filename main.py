import sys
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit, QLCDNumber, QLabel, QMainWindow
import PyQt5.QtGui as QtGui
from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from circles import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)
        self.x = self.y = self.d = 0
        self.color1 = randint(0, 255)
        self.color2 = randint(0, 255)
        self.color3 = randint(0, 255)

    def run(self):
        self.color1 = randint(0, 255)
        self.color2 = randint(0, 255)
        self.color3 = randint(0, 255)
        self.x = self.y = self.d = randint(1, 500)
        self.paintEvent(self.event)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        qp.setBrush(QColor(self.color1, self.color2, self.color3))
        qp.drawEllipse(self.x, self.y, self.d, self.d)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
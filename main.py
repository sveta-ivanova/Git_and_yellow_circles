import sys
from PyQt5 import uic  # Импортируем uic
from random import randint
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QButtonGroup, QVBoxLayout
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)  # Загружаем дизайн
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_ellipse(self, qp):
        x = randint(1, 580)
        y = randint(1, 320)
        qp.setBrush(QColor(255, 255, 0))
        w = randint(1, 100)
        qp.drawEllipse(x, y, w, w)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

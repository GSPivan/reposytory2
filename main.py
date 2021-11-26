import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic


class krug(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)
        self.pushButton.clicked.connect(self.risov)

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw(qp)
        # Завершаем рисование
        qp.end()

    def draw(self, qp):
        rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        qp.setBrush(QColor(rgb[0], rgb[1], rgb[2]))
        x = random.randint(0, 150)
        y = random.randint(0, 150)
        x1 = random.randint(0, 150)
        y1 = random.randint(0, 150)
        qp.drawEllipse(x, y, x1, y1)

    def risov(self):
        self.repaint()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = krug()
    ex.show()
    sys.exit(app.exec())

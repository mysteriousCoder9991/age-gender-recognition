import os
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Age - Gender Detector 2.0'
        self.left = 500
        self.top = 250
        self.width = 420
        self.height = 150
        self.setStyleSheet("background-color: cyan;")
        self.setMaximumSize(420, 150)

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        startButton = QPushButton('Start', self)
        exitButton = QPushButton('Exit', self)
        footerLabel = QLabel(" © Rahul Dhar , 2021 ", self)

        startButton.setStyleSheet("background-color: white;")
        exitButton.setStyleSheet("background-color: white;")
        footerLabel.setStyleSheet("background-color:#808080;")

        startButton.setToolTip('To start the application please click this')
        exitButton.setToolTip('To exit from the application please click this')

        startButton.move(175, 50)
        exitButton.move(175, 80)
        footerLabel.move(5, 135)

        startButton.clicked.connect(self.on_click)
        exitButton.clicked.connect(self.on_click1)

        self.show()

    @pyqtSlot()
    def on_click(self):
        os.system("python gad.py")

    @pyqtSlot()
    def on_click1(self):
        print("Thank you for using this application.This is made by Rahul Dhar")
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

import os
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Age-Gender-Detection '
        self.left = 500
        self.top = 250
        self.width = 420
        self.height = 150
        self.setStyleSheet("background-color: cyan;")

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        startButton = QPushButton('Start the Application', self)
        exitButton = QPushButton('Exit the Application', self)

        startButton.setStyleSheet("background-color: white;")
        exitButton.setStyleSheet("background-color: white;")

        startButton.setToolTip('This is start button')
        exitButton.setToolTip('This is the exit button')

        startButton.move(150, 50)
        exitButton.move(150, 80)

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

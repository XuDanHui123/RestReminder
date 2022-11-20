import sys
import ui_setting
import configparser
from PyQt5.QtWidgets import *


class Main(QMainWindow, ui_setting.Ui_MainWindow):

    def save(self):
        self.ini.set('home', 'between', str(self.between.value()))
        print(self.between.value())
        self.ini.set('home', 'last', str(self.last.value()))
        print(self.last.value())
        self.ini.write(open("config.ini", "w"))
        self.close()

    def __init__(self):
        QMainWindow.__init__(self)
        ui_setting.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.ini = configparser.ConfigParser()
        self.ini.read("./config.ini", encoding='utf-8')
        between = self.ini.getint('home', 'between')
        last = self.ini.getint('home', 'last')
        self.between.setMaximum(1000)
        self.between.setProperty("value", between)
        self.last.setMaximum(30)
        self.last.setProperty("value", last)
        self.pushButton.clicked.connect(self.save)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

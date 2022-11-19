import sys
import ui_setting
import configparser
from PyQt5.QtWidgets import *


class Main(QMainWindow, ui_setting.Ui_MainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        ui_setting.Ui_MainWindow.__init__(self)
        self.setupUi(self)
        ini = configparser.ConfigParser()
        ini.read("./config.ini", encoding='utf-8')
        between = ini.getint('home', 'between')
        last = ini.getint('home', 'last')
        self.between.setMaximum(1000)
        self.between.setProperty("value", between)
        self.last.setMaximum(30)
        self.last.setProperty("value", last)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

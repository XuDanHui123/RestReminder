import win10toast
import os
import configparser

class init():
    def __init__(self):
        self.ini = configparser.ConfigParser();
        self.ini.read("./config.ini", encoding='utf-8')
        used = self.ini.getint('home','used')
        if(used==0):
            del self.ini
            os.system("setting.py")
            self.ini = configparser.ConfigParser();
            self.ini.read("./config.ini", encoding='utf-8')
            self.ini.set('home', 'used', '1')
            self.ini.write(open("config.ini", "w"))
    def rest(self):
        pass
if __name__ == '__main__':
    init()
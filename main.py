import os
import time
import configparser
import getpass
import sys


class init():
    def __init__(self):
        self.username = getpass.getuser()
        self.fileroot = sys.argv[0]
        self.ini = configparser.ConfigParser()
        self.ini.read("./config.ini", encoding='utf-8')
        used = self.ini.getint('home', 'used')
        if (used == 0):
            self.firsyUse()
        self.rest()

    def rest(self):
        while True:
            time.sleep(self.ini.getint('home', 'between')*60)
            os.system('rest_scr.exe')
            time.sleep(self.ini.getint('home', 'last')*60)

    def firsyUse(self):
        del self.ini
        os.system('setting.exe')
        self.ini = configparser.ConfigParser()
        self.ini.read("./config.ini", encoding='utf-8')
        self.ini.set('home', 'used', '1')
        self.ini.write(open("config.ini", "w"))
        root = 'C:\\Users\\'+self.username+'\\AppData\\Local\\RestReminder'
        os.system('mkdir ' + root)
        print('type nul> '+root+'\\root.txt')
        os.system('type nul> '+root+'\\root.txt')
        os.system('echo '+self.fileroot+'> ' + root + '\\root.txt')
        # os.system('''copy startup.bat "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"''')


if __name__ == '__main__':
    init()

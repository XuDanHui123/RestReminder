from multiprocessing import Process
import os
import time
import tkinter
import configparser
import setting
# import heartrate

# heartrate.trace(browser=True)
class init():
    def __init__(self):
        self.ini = configparser.ConfigParser();
        self.ini.read("./config.ini", encoding='utf-8')
        used = self.ini.getint('home','used')
        if(used==0):
            del self.ini
            os.system('setting.exe')
            self.ini = configparser.ConfigParser();
            self.ini.read("./config.ini", encoding='utf-8')
            self.ini.set('home', 'used', '1')
            self.ini.write(open("config.ini", "w"))
        # self.rest()

    def rest(self):
        while True:
            time.sleep(self.ini.getint('home','between')*60)
            os.system('black.py')
            time.sleep(self.ini.getint('home','last')*60)

if __name__ == '__main__':
    init()
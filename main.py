from multiprocessing import Process
import os
import time
import tkinter
import configparser
# import heartrate

# heartrate.trace(browser=True)
class init():
    def __init__(self):
        self.ini = configparser.ConfigParser();
        self.ini.read("./config.ini", encoding='utf-8')
        used = self.ini.getint('home','used')
        if(used==0):
            del self.ini
            print('s')
            os.system("setting.py")
            print('e')
            self.ini = configparser.ConfigParser();
            self.ini.read("./config.ini", encoding='utf-8')
            self.ini.set('home', 'used', '1')
            self.ini.write(open("config.ini", "w"))
        # self.rest()

    def rest(self):
        while True:
            print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
            time.sleep(self.ini.getint('home','between')*60)
            print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
            p = Process(target=self.scr,args=())
            p.start()
            time.sleep(self.ini.getint('home','last')*60)
            print(time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime()))
            self.root.destroy()

if __name__ == '__main__':
    init()
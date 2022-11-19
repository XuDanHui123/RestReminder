import win10toast
import configparser

class init():
    def __init__(self):
        ini = configparser.ConfigParser();
        ini.read("./config.ini", encoding='utf-8')
        global time
        time = ini.getint('home','time')
        used = ini.getini('home','used')
        if(used==0):
            pass
if __name__ == '__main__':
    init()
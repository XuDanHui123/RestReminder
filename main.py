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
            os.system("setting.py")
            self.ini = configparser.ConfigParser();
            self.ini.read("./config.ini", encoding='utf-8')
            self.ini.set('home', 'used', '1')
            self.ini.write(open("config.ini", "w"))
        self.rest()

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

    def scr(self):
        self.root = tkinter.Tk()
        # self.root.overrideredirect(True)  #pull时删除此句注释
        self.root.config(bg="Black")
        length_1 = self.root.winfo_screenheight()
        width_1 = self.root.winfo_screenwidth()
        self.root.geometry(str(width_1) + "x" + str(length_1))
        # self.root.wm_attributes("-topmost", 1)
        ini = configparser.ConfigParser()   
        ini.read("./config.ini", encoding='utf-8')
        last = ini.getint('home', 'last')
        rest_label = tkinter.Label(text="Have a rest for " + str(last) + " minute(s)",
                                  bg='black',
                                  fg='white',
                                  font=("Consolas", 36)
                                  )
        rest_label.place(relx=.5, rely=.5, anchor=tkinter.CENTER)
        self.root.mainloop()

if __name__ == '__main__':
    init()
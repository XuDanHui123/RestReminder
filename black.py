import tkinter
import threading
import configparser
import time

print('s')


def close():
    time.sleep(last * 60)
    root.destroy()
    return


root = tkinter.Tk()
root.overrideredirect(True)
root.config(bg="Black")
length_1 = root.winfo_screenheight()
width_1 = root.winfo_screenwidth()
root.geometry(str(width_1) + "x" + str(length_1))
root.wm_attributes("-topmost", 1)
ini = configparser.ConfigParser()
ini.read("./config.ini", encoding='utf-8')
last = ini.getint('home', 'last')
rest_label = tkinter.Label(text="Have a rest for " + str(last) + " minute(s)",
                           bg='black',
                           fg='white',
                           font=("Consolas", 36))
rest_label.place(relx=.5, rely=.5, anchor=tkinter.CENTER)
skip_bnt = tkinter.Button(text=" ◀ Skip Rest",
                          command=root.destroy,
                          bg='black',
                          fg='white',
                          font=('Consolas', 16))
skip_bnt.place(relx=.1, rely=.9, anchor=tkinter.CENTER)
tip_label = tkinter.Label(
                          text='by XuDanhui',
                          font=('Consolas', 13),
                          bg='black',
                          fg='white')
tip_label.place(relx=.5, rely=.95)
threading.Thread(target=close, args=()).start()
root.mainloop()

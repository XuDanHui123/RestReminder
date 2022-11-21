import tkinter
import configparser

root = tkinter.Tk() 
# root.overrideredirect(True) #pull时删除此句注释
root.config(bg="Black")
length_1 = root.winfo_screenheight()
width_1 = root.winfo_screenwidth()
root.geometry(str(width_1) + "x" + str(length_1))
# root.wm_attributes("-topmost", 1)
ini = configparser.ConfigParser()
ini.read("./config.ini", encoding='utf-8')
last = ini.getint('home', 'last')
rest_label = tkinter.Label(text="Have a rest for " + str(last) + " minute(s)",
                           bg='black',
                           fg='white',
                           font = ("Consolas", 36)
                           )
rest_label.place(relx=.5, rely=.5,anchor= tkinter.CENTER)
root.mainloop()

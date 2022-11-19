import tkinter

root = tkinter.Tk()
root.overrideredirect(True)
root.config(bg="Black")
length_1 = root.winfo_screenheight()
width_1 = root.winfo_screenwidth()
root.geometry(str(width_1)+"x"+str(length_1))
root.wm_attributes("-topmost", 1)

root.mainloop()

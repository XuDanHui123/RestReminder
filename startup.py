import getpass
import os
root = 'C:\\Users\\'+getpass.getuser()+'\\AppData\\Local\\RestReminder'
exe = open(root+'\\root.txt').readline().strip()
print(exe)
os.system(exe)
# Dwelcomescreen page
from tkinter import *
from tkinter import PhotoImage
import os

root=Tk()
x = int((root.winfo_screenwidth() - 1000) / 2)
y = int((root.winfo_screenheight() - 800) / 2)
root.geometry(f'1000x800+{x}+{y}')
root.title("Dhawal's Welcome Screen")
root.overrideredirect(True)
def afterIT():
    root.quit()  
root.bg_img=PhotoImage(file='images/welcomescreen.png')
bg=Label(root, image=root.bg_img,border=0)
bg.place(x=0,y=0)

root.after(7000,afterIT)

root.mainloop()

root.destroy()
try:
    os.system("python Dlogin.py")
except Exception as e:
    print("Error >>>" , e)
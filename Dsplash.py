# Dsplash page
from tkinter import *
import time
from customtkinter import *

root = Tk()
x = int((root.winfo_screenwidth() - 1042) / 2)
y = int((root.winfo_screenheight() -1042) / 2)

root.geometry(f'1042x1042+{x}+{y}')
root.config(bg="white")
root.overrideredirect(True)

root.wm_attributes("-topmost",True)
root.lift()
root.wm_attributes("-topmost",True)
root.wm_attributes("-disabled",True)
root.wm_attributes("-transparentcolor","white")

img = PhotoImage(file="images/splash.png")
main_pic = Label(image=img,bg="white",border=0,fg='white')
main_pic.place(x=0,y=0)

def closeIT():
    root.destroy()
    import Dprogressbar
root.after(3000,closeIT)
root.mainloop()
#Dlogin page

#modules------------------------------------------------------------------
import tkinter
import customtkinter
from PIL import Image
import mysql.connector as ms
from tkinter import messagebox
import os
import pickle
#------------------------------------------------------------------------


#database_connection-----------------------------------------------------
conn = ms.connect(host="localhost",user="root",database="digbydhawal")
cur = conn.cursor()
#------------------------------------------------------------------------


#window_configuration----------------------------------------------------
customtkinter.set_appearance_mode("Light")
root = customtkinter.CTk()
x = int((root.winfo_screenwidth() - 800) / 2)
y = int((root.winfo_screenheight() - 400) / 2)
root.geometry(f'800x400+{x}+{y}')
root.title('Login')
root.resizable(False,False)
root.protocol("WM_DELETE_WINDOW", quit)
#------------------------------------------------------------------------


#backend-----------------------------------------------------------------
def login(x=0):
    username = entry1.get()
    password = entry2.get()
    cur.execute(f"SELECT COUNT(*) FROM user WHERE username = '{username}' AND password = '{password}' ")
    data = cur.fetchall()
    if data[0][0] == 1:
        logs = [username,password]
        with open('Main/logs/log.bkl','wb') as log_file:
            pickle.dump(logs,log_file)
        messagebox.showinfo("Success","Login Successfull.")
        root.quit()
        root.destroy()
        os.system("python Main/dig_home_page.py")
    if data[0][0] == 0:
        messagebox.showwarning("Failed","Invalid credentials! Please try again")                      

def show_password():
    global flag1,show_img,show_pass,entry2
    if flag1:
        entry2.configure(show = "")
        show_img = customtkinter.CTkImage(light_image=Image.open("images/close_eye.png"),dark_image=Image.open("images/close_eye.png"),size=(27.52,16))
        show_pass.configure(image=show_img)
        flag1 = False
    else:
        entry2.configure(show = "*")
        show_img = customtkinter.CTkImage(light_image=Image.open("images/show_eye.png"),dark_image=Image.open("images/show_eye.png"),size=(27.52,16))
        show_pass.configure(image=show_img)
        flag1 = True

def register():
    root.quit()
    root.destroy()
    os.system("python Dregister.py")
#------------------------------------------------------------------------


#frontend----------------------------------------------------------------
img1 = customtkinter.CTkImage(light_image=Image.open("pattern.png"),dark_image=Image.open("pattern.png"),size=(800,400))
l1=customtkinter.CTkLabel(master=root,image=img1)
l1.pack()

img2 = customtkinter.CTkImage(light_image=Image.open("images/login.png"),dark_image=Image.open("images/login.png"),size=(400,400))
side_image=customtkinter.CTkLabel(master=root,image=img2,text="")
side_image.place(relx=0.5,rely=0.5,anchor=tkinter.E)

frame=customtkinter.CTkFrame(master=l1, width=400, height=400, corner_radius=15,fg_color="#f2f2f2")
frame.place(relx=0.5, rely=0.5, anchor=tkinter.W)

l2=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic Bold',30),text_color="#f0989d")
l2.place(relx=0.5, y=50,anchor=tkinter.CENTER)

entry1=customtkinter.CTkEntry(master=frame, width=220,placeholder_text_color='#f0989d',border_color='#f0989d', placeholder_text='Username')
entry1.place(relx=0.5, y=150,anchor=tkinter.CENTER)
entry1.bind("<Enter>", lambda event:entry1.configure(placeholder_text_color="#7c696e",border_color='#7c696e'))
entry1.bind("<Leave>", lambda event:entry1.configure(placeholder_text_color="#f0989d",border_color='#f0989d'))
entry1.bind("<Return>",login)

entry2=customtkinter.CTkEntry(master=frame, width=220,placeholder_text_color='#f0989d',border_color='#f0989d', placeholder_text='Password',show="*")
entry2.place(relx=0.5, y=205,anchor=tkinter.CENTER)
entry2.bind("<Enter>", lambda event:entry2.configure(placeholder_text_color="#7c696e",border_color='#7c696e'))
entry2.bind("<Leave>", lambda event:entry2.configure(placeholder_text_color="#f0989d",border_color='#f0989d'))
entry2.bind("<Return>",login)

flag1 = True

show_img = customtkinter.CTkImage(light_image=Image.open("images/show_eye.png"),dark_image=Image.open("images/show_eye.png"),size=(27.52,16))
show_pass = customtkinter.CTkButton(master=entry2,image=show_img,text="",width=27.52,height=16,border_spacing=0,fg_color="white",hover_color="white",corner_radius=50,command=show_password)
show_pass.place(relx=0.76,rely=0.5,anchor=tkinter.W)

register_button=customtkinter.CTkButton(master=frame, command=register, text="Not having any account? Make one.",font=('Century Gothic',12),fg_color="#f2f2f2",text_color="#f0989d",hover_color="#f2f2f2")
register_button.place(relx=0.5,y=255,anchor=tkinter.CENTER)
register_button.bind("<Enter>",lambda event: register_button.configure(text_color="#7c696e"))
register_button.bind("<Leave>",lambda event: register_button.configure(text_color="#f0989d"))

login_button = customtkinter.CTkButton(master=frame, width=220,text="Login", command=login, border_width=3, corner_radius=25,font=('Century Gothic Bold',12),fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d")
login_button.place(relx=0.5, y=300,anchor=tkinter.CENTER)
login_button.bind("<Enter>",lambda event: login_button.configure(fg_color="#7c696e",text_color="#f2f2f2",border_width=0))
login_button.bind("<Leave>",lambda event: login_button.configure(fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d",border_width=3))
#------------------------------------------------------------------------


root.mainloop()

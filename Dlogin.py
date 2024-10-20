import tkinter
import customtkinter
from PIL import ImageTk,Image
import mysql.connector as ms
from tkinter import messagebox
import os


conn = ms.connect(host="localhost",user="root",database="digbydhawal")
cur = conn.cursor()

 


root = customtkinter.CTk()
x = int((root.winfo_screenwidth() - 800) / 2)
y = int((root.winfo_screenheight() - 400) / 2)
root.geometry(f'800x400+{x}+{y}')
root.title('Login')
root.resizable(False,False)




def login(x=0):
    username = entry1.get()
    password = entry2.get()
    cur.execute("SELECT * FROM user")
    data = cur.fetchall()
    for i in data:
        if i[1] == username:
            if i[2] == password:
                messagebox.showinfo("Success","Login Successfull.")
                root.quit()
                os.system('show_eye.png')
            else:
                messagebox.showwarning("Failed","Password isn't matching!Please try again")           

img1 = customtkinter.CTkImage(light_image=Image.open("pattern.png"),dark_image=Image.open("pattern.png"),size=(800,400))
# img1=ImageTk.PhotoImage(Image.open("pattern.png"))
l1=customtkinter.CTkLabel(master=root,image=img1)
l1.pack()
img2 = customtkinter.CTkImage(light_image=Image.open("images/login.png"),dark_image=Image.open("images/login.png"),size=(400,400))
# img2=ImageTk.PhotoImage(Image.open("images/login.png"))
l2=customtkinter.CTkLabel(master=root,image=img2,text="")
l2.place(relx=0.5,rely=0.5,anchor=tkinter.E)

#creating custom frame
frame=customtkinter.CTkFrame(master=l1, width=400, height=400, corner_radius=15,fg_color="#f2f2f2")
frame.place(relx=0.5, rely=0.5, anchor=tkinter.W)

l2=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic Bold',30),text_color="#f0989d")
l2.place(relx=0.5, y=50,anchor=tkinter.CENTER)



entry1=customtkinter.CTkEntry(master=frame, width=220,placeholder_text_color='#f0989d',border_color='#f0989d', placeholder_text='Username')
entry1.place(relx=0.5, y=150,anchor=tkinter.CENTER)
entry1.bind("<Enter>", lambda event:entry1.configure(placeholder_text_color="#7c696e",border_color='#7c696e'))
entry1.bind("<Leave>", lambda event:entry1.configure(placeholder_text_color="#f0989d",border_color='#f0989d'))
entry2=customtkinter.CTkEntry(master=frame, width=220,placeholder_text_color='#f0989d',border_color='#f0989d', placeholder_text='Password', show="*")
entry2.place(relx=0.5, y=205,anchor=tkinter.CENTER)
entry2.bind("<Enter>", lambda event:entry2.configure(placeholder_text_color="#7c696e",border_color='#7c696e'))
entry2.bind("<Leave>", lambda event:entry2.configure(placeholder_text_color="#f0989d",border_color='#f0989d'))
entry2.bind("<Return>",login)
show_img = customtkinter.CTkImage(light_image=Image.open("show_eye.png"),dark_image=Image.open("show_eye.png"),size=(10,10))
show_pass = customtkinter.CTkButton(master=entry2,image=show_img,corner_radius=500,text="",width=5,height=5)
show_pass.place(relx=0.85,rely=0.5,anchor=tkinter.W)

def test():
    print("test")

register_button=customtkinter.CTkButton(master=frame, command=test, text="Not having any account? Make one.",font=('Century Gothic',12),fg_color="#f2f2f2",text_color="#f0989d",hover_color="#f2f2f2")
register_button.place(relx=0.5,y=255,anchor=tkinter.CENTER)
register_button.bind("<Enter>",lambda event: register_button.configure(text_color="#7c696e"))
register_button.bind("<Leave>",lambda event: register_button.configure(text_color="#f0989d"))

#Create custom button
login_button = customtkinter.CTkButton(master=frame, width=220,
 text="Login", command=login, border_width=3,
 corner_radius=25,font=('Century Gothic Bold',12)
 ,fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d")
login_button.place(relx=0.5, y=300,anchor=tkinter.CENTER)
login_button.bind("<Enter>",lambda event: login_button.configure(fg_color="#7c696e",text_color="#f2f2f2",border_width=0))
login_button.bind("<Leave>",lambda event: login_button.configure(fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d",border_width=3))

root.mainloop()

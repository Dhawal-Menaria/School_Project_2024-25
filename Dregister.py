#Dregister page

#modules------------------------------------------------------------------
import tkinter
import customtkinter
from PIL import Image
import mysql.connector as ms
from tkinter import messagebox
import os
import pickle
from tkcalendar import DateEntry
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
root.title('Register')
root.resizable(False,False)
root.protocol("WM_DELETE_WINDOW", quit)

#------------------------------------------------------------------------


#backend-----------------------------------------------------------------
def register(x=0):
    fullname = entry1.get()
    username = entry2.get()
    email = entry3.get()
    password = entry4.get()
    conpass = entry5.get()
    gender_value = gender.get()
    dob = date_of_bith.get_date()
    fin_gender = ""
    if gender_value == 1:
        fin_gender = "M"
    if gender_value == 2:
        fin_gender = "F"

    if username == "" or password == "" or email == "" or fullname == "" or gender == "":
        messagebox.showwarning("Insufficient Details","Please fill all the details required")
        return
    cur.execute("SELECT * FROM user")
    data = cur.fetchall()
    for i in data:
        if i[1] == username:
            messagebox.showwarning("Username unavailable","Username is already taken")
            return
    if "@" not in email and ".com" not in email:
        messagebox.showwarning("Email isn't applicable","Please give an valid email.")
        return
    if flag1 and password!=conpass:
        messagebox.showwarning("Password cofirmaiton failed","Please enter password same in confirmation.")
        return
    else:
        cur.execute(f"INSERT INTO user(username,password,full_name,email,gender,date_of_birth) VALUES('{username}','{password}','{fullname}','{email}','{fin_gender}','{dob}')")
        conn.commit()
        logs = [username,password]
        with open('Main/logs/log.bkl','wb') as log_file:
            pickle.dump(logs,log_file)
        messagebox.showinfo("Account Created","Your Account has been created successfully.")
        conn.close()
        root.quit()
        root.destroy()
        os.system("python Main/dig_home_page.py")

def show_password():
    global flag1,show_img,show_pass,entry4,entry5
    if flag1:
        entry4.configure(show = "")
        entry5.place(x=0,y=800)
        gender_date_frame.place(relx=0.5,y=240,anchor=tkinter.CENTER)
        login_button.place(relx=0.5,y=280,anchor=tkinter.CENTER)
        register_button.place(relx=0.5, y=320,anchor=tkinter.CENTER)
        show_img = customtkinter.CTkImage(light_image=Image.open("images/close_eye.png"),dark_image=Image.open("images/close_eye.png"),size=(27.52,16))
        show_pass.configure(image=show_img)
        flag1 = False
    else:
        entry4.configure(show = "*")
        entry5.place(relx=0.5, y=240,anchor=tkinter.CENTER)
        gender_date_frame.place(relx=0.5,y=280,anchor=tkinter.CENTER)
        login_button.place(relx=0.5,y=320,anchor=tkinter.CENTER)
        register_button.place(relx=0.5, y=360,anchor=tkinter.CENTER)
        show_img = customtkinter.CTkImage(light_image=Image.open("images/show_eye.png"),dark_image=Image.open("images/show_eye.png"),size=(27.52,16))
        show_pass.configure(image=show_img)
        flag1 = True

def login():
    root.quit()
    root.destroy()
    os.system("python Dlogin.py")
#------------------------------------------------------------------------


#frontend----------------------------------------------------------------
img1 = customtkinter.CTkImage(light_image=Image.open("pattern.png"),dark_image=Image.open("pattern.png"),size=(800,400))
l1=customtkinter.CTkLabel(master=root,image=img1)
l1.pack()

img2 = customtkinter.CTkImage(light_image=Image.open("images/register.png"),dark_image=Image.open("images/register.png"),size=(400,400))
side_image=customtkinter.CTkLabel(master=root,image=img2,text="")
side_image.place(relx=0.5,rely=0.5,anchor=tkinter.W)

frame=customtkinter.CTkFrame(master=l1, width=400, height=400, corner_radius=15,fg_color="#f2f2f2")
frame.place(relx=0.5, rely=0.5, anchor=tkinter.E)

l2=customtkinter.CTkLabel(master=frame, text="Register Yourself",font=('Century Gothic Bold',30),text_color="#f0989d")
l2.place(relx=0.5, y=20, anchor=tkinter.CENTER)

entry1=customtkinter.CTkEntry(master=frame, width=220,placeholder_text_color='#f0989d',border_color='#f0989d', placeholder_text='Full Name')
entry1.place(relx=0.5, y=80,anchor=tkinter.CENTER)
entry1.bind("<Enter>", lambda event:entry1.configure(placeholder_text_color="#7c696e",border_color='#7c696e'))
entry1.bind("<Leave>", lambda event:entry1.configure(placeholder_text_color="#f0989d",border_color='#f0989d'))
entry1.bind("<Return>",register)

entry2=customtkinter.CTkEntry(master=frame, width=220,placeholder_text_color='#f0989d',border_color='#f0989d', placeholder_text='Username')
entry2.place(relx=0.5, y=120,anchor=tkinter.CENTER)
entry2.bind("<Enter>", lambda event:entry2.configure(placeholder_text_color="#7c696e",border_color='#7c696e'))
entry2.bind("<Leave>", lambda event:entry2.configure(placeholder_text_color="#f0989d",border_color='#f0989d'))
entry2.bind("<Return>",register)

entry3=customtkinter.CTkEntry(master=frame, width=220,placeholder_text_color='#f0989d',border_color='#f0989d', placeholder_text='Email')
entry3.place(relx=0.5, y=160,anchor=tkinter.CENTER)
entry3.bind("<Enter>", lambda event:entry3.configure(placeholder_text_color="#7c696e",border_color='#7c696e'))
entry3.bind("<Leave>", lambda event:entry3.configure(placeholder_text_color="#f0989d",border_color='#f0989d'))
entry3.bind("<Return>",register)

entry4=customtkinter.CTkEntry(master=frame, width=220,placeholder_text_color='#f0989d',border_color='#f0989d', placeholder_text='Password',show="*")
entry4.place(relx=0.5, y=200,anchor=tkinter.CENTER)
entry4.bind("<Enter>", lambda event:entry4.configure(placeholder_text_color="#7c696e",border_color='#7c696e'))
entry4.bind("<Leave>", lambda event:entry4.configure(placeholder_text_color="#f0989d",border_color='#f0989d'))
entry4.bind("<Return>",register)

entry5=customtkinter.CTkEntry(master=frame, width=220,placeholder_text_color='#f0989d',border_color='#f0989d', placeholder_text='Confirm Password',show="*")
entry5.place(relx=0.5, y=240,anchor=tkinter.CENTER)
entry5.bind("<Enter>", lambda event:entry5.configure(placeholder_text_color="#7c696e",border_color='#7c696e'))
entry5.bind("<Leave>", lambda event:entry5.configure(placeholder_text_color="#f0989d",border_color='#f0989d'))
entry5.bind("<Return>",register)

flag1 = True

show_img = customtkinter.CTkImage(light_image=Image.open("images/show_eye.png"),dark_image=Image.open("images/show_eye.png"),size=(27.52,16))
show_pass = customtkinter.CTkButton(master=entry4,image=show_img,text="",width=27.52,height=16,border_spacing=0,fg_color="white",hover_color="white",corner_radius=50,command=show_password)
show_pass.place(relx=0.76,rely=0.5,anchor=tkinter.W)

gender = tkinter.IntVar()
gender_date_frame=customtkinter.CTkFrame(master=frame, width=300, height=40, corner_radius=15,fg_color="#f2f2f2")
gender_date_frame.place(relx=0.5,y=280,anchor=tkinter.CENTER)
male_gender = customtkinter.CTkRadioButton(master=gender_date_frame,fg_color="#7c696e",border_color="#f0989d",text_color="#f0989d",hover_color="#7c696e",text="Male",value=1,variable=gender,font=('Century Gothic',12))
female_gender = customtkinter.CTkRadioButton(master=gender_date_frame,fg_color="#7c696e",border_color="#f0989d",text_color="#f0989d",hover_color="#7c696e",text="Female",value=2,variable=gender,font=('Century Gothic',12))
date_of_bith=DateEntry(gender_date_frame,width=12,border=0)
male_gender.place(relx=0.2,rely=0.5,anchor=tkinter.CENTER)
female_gender.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
date_of_bith.place(relx=0.8,rely=0.5,anchor=tkinter.CENTER)


login_button=customtkinter.CTkButton(master=frame, command=login, text="Already have an account? Go to Login.",font=('Century Gothic',12),fg_color="#f2f2f2",text_color="#f0989d",hover_color="#f2f2f2")
login_button.place(relx=0.5,y=320,anchor=tkinter.CENTER)
login_button.bind("<Enter>",lambda event: login_button.configure(text_color="#7c696e"))
login_button.bind("<Leave>",lambda event: login_button.configure(text_color="#f0989d"))

register_button = customtkinter.CTkButton(master=frame, width=220,text="Register", command=register, border_width=3, corner_radius=25,font=('Century Gothic Bold',12),fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d",height=25)
register_button.place(relx=0.5, y=360,anchor=tkinter.CENTER)
register_button.bind("<Enter>",lambda event: register_button.configure(fg_color="#7c696e",text_color="#f2f2f2",border_width=0))
register_button.bind("<Leave>",lambda event: register_button.configure(fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d",border_width=3))
#------------------------------------------------------------------------


root.mainloop()





#Modules--------------------------------------
import customtkinter
import tkinter
from PIL import Image
import pickle
import mysql.connector as ms
import os 
#---------------------------------------------


#Window_configuration-------------------------
root = customtkinter.CTk()

wow = root.winfo_screenwidth()
how = root.winfo_screenheight()

x = int((wow*0.2) / 2)
y = int((how*0.2) / 2)
root.geometry(f'{int(wow*0.8)}x{int(how*0.8)}+{x}+{y}')
root.title('Home | Dig')
root.resizable(False,False)
root.protocol("WM_DELETE_WINDOW", quit)
#---------------------------------------------

#Backend--------------------------------------
with open("Main/logs/log.bkl",'rb') as f:
    data = pickle.load(f)[0]
conn = ms.connect(host="localhost",user="root",database="digbydhawal")
cur = conn.cursor()
#---------------------------------------------



#Frontend-------------------------------------
top_frame = customtkinter.CTkFrame(master=root,width=int(wow*0.8),height=75,corner_radius=0)
top_frame.pack(side="top")
logo_image = customtkinter.CTkImage(light_image=Image.open("./images/logo.png"),dark_image=Image.open("./images/logo.png"),size=(50,48.4))
l1 = customtkinter.CTkLabel(master=top_frame,image=logo_image,text="")
l1.place(anchor=tkinter.NW,x=20,y=14)


search_frame = customtkinter.CTkFrame(master=top_frame,width=int(wow*0.5),fg_color="#ebebeb",)
search_frame.place(relx=0.5,rely=0.5,anchor=tkinter.CENTER)
search = customtkinter.CTkEntry(master=search_frame,placeholder_text="Search ...",font=("Century Gothic",15),width=500,height=40)
search.grid(row=0,column=0)
search_icon = customtkinter.CTkImage(light_image=Image.open("./images/search.png"),dark_image=Image.open("./images/search.png"),size=(41,40))
search_button = customtkinter.CTkButton(master=search_frame,text="",image=search_icon,width=41,corner_radius=50)
search_button.grid(row=0,column=1)



#Menu_Option----------------------------------
menu_image = customtkinter.CTkImage(light_image=Image.open("./images/menu.png"),dark_image=Image.open("./images/menu.png"),size=(40,40))
profile = customtkinter.CTkImage(light_image=Image.open("./images/profile.png"),dark_image=Image.open("./images/profile.png"),size=(40,40))
logout = customtkinter.CTkImage(light_image=Image.open("./images/logout.png"),dark_image=Image.open("./images/logout.png"),size=(40,40))
create = customtkinter.CTkImage(light_image=Image.open("./images/create.png"),dark_image=Image.open("./images/create.png"),size=(40,40))
options = [profile,logout,create]
def toggle_dropdown():
    if dropdown_menu.winfo_viewable():
        dropdown_menu.withdraw()  
    else:
        position_dropdown()  
def select_option():
    print("conn")
    dropdown_menu.withdraw()
def position_dropdown():
    x = menu.winfo_rootx()
    y = menu.winfo_rooty() + menu.winfo_height()
    dropdown_menu.geometry(f"+{x}+{y}")
    dropdown_menu.deiconify() 

menu = customtkinter.CTkButton(top_frame, image=menu_image,text="", command=toggle_dropdown,width=20,hover=False,fg_color="#ebebeb")
menu.place(relx=0.9,anchor=tkinter.NW,y=14)

dropdown_menu = tkinter.Toplevel(root)
dropdown_menu.overrideredirect(True) 
dropdown_menu.withdraw()  

for img in options:
    option_button = customtkinter.CTkButton(dropdown_menu, image=img, text="", compound="left",command=select_option,width=20,hover=False,fg_color="#ebebeb")
    option_button.pack(fill="x", anchor="w")
#---------------------------------------------
a = customtkinter.CTkLabel(master = root,text="_"*int(wow*0.8))
a.pack(side="top")


#Side_Frame-----------------------------------
side_frame = customtkinter.CTkFrame(master=root,border_color="black",height=int(how*0.55),width=int(wow*0.15),border_width=1,fg_color="#ebebeb")
side_frame.pack(side="left")

home_btn = customtkinter.CTkButton(master=side_frame,text="Home",text_color="#7c696e",fg_color="#ebebeb",hover=False)
home_btn.place(relx=0.5,anchor=tkinter.CENTER,y=50)
people_btn = customtkinter.CTkButton(master=side_frame,text="People",text_color="#7c696e",fg_color="#ebebeb",hover=False)
people_btn.place(relx=0.5,anchor=tkinter.CENTER,y=100)
help_btn = customtkinter.CTkButton(master=side_frame,text="help",text_color="#7c696e",fg_color="#ebebeb",hover=False)
help_btn.place(relx=0.5,anchor=tkinter.CENTER,y=150)
about_btn = customtkinter.CTkButton(master=side_frame,text="about",text_color="#7c696e",fg_color="#ebebeb",hover=False)
about_btn.place(relx=0.5,anchor=tkinter.CENTER,y=200)
#---------------------------------------------


#Post_Frame-----------------------------------
post_frame = customtkinter.CTkScrollableFrame(master=root,border_color="black",height=int(how*0.55),width=int(wow*0.55),border_width=1,fg_color="#ebebeb")
top_frame.pack(side="top")
cur.execute(f"SELECT * FROM post")
post = cur.fetchall()[::-1]
for i in post:
    post = customtkinter.CTkScrollableFrame(master=post_frame,width=int(wow*0.55),height=int(how*0.15),scrollbar_button_hover_color="#ebebeb",scrollbar_button_color="#ebebeb",fg_color="#ebebeb")
    post.pack(pady=5)
    if i[1] == data:
        user = "You"
    else:
        user = i[1]
    username = customtkinter.CTkLabel(master=post,text=f"{user}",font=("Century Gothic",15))
    username.pack(anchor=tkinter.W)
    title = customtkinter.CTkLabel(master=post,text=f"{i[0]}",font=("Century Gothic Bold",20))
    title.pack(anchor=tkinter.W)
    desc = customtkinter.CTkLabel(master=post,text=f"{i[3]}",font=("Century Gothic",15))
    desc.pack(anchor=tkinter.W)
    time = customtkinter.CTkLabel(master=post,text=f"{i[2]}",font=("Century Gothic",10))
    time.pack(anchor=tkinter.W)

#---------------------------------------------

#---------------------------------------------
root.mainloop()
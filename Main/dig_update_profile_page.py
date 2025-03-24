import customtkinter
import tkinter
from PIL import Image
import pickle
import mysql.connector as ms
import os
from tkcalendar import DateEntry
from tkinter import messagebox
root = customtkinter.CTk()
customtkinter.set_appearance_mode("Light")
wow = root.winfo_screenwidth()
how = root.winfo_screenheight()

x = int((wow * 0.2) / 2)
y = int((how * 0.2) / 2)
root.geometry(f'{int(wow * 0.8)}x{int(how * 0.8)}+{x}+{y}')
root.title('Profile | Dig')
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", quit)
root.config(bg="#f2f2f2")


with open("Main/logs/log.bkl", 'rb') as f:
    data = pickle.load(f)[0]
conn = ms.connect(host="localhost", user="root", database="digbydhawal")
cur = conn.cursor()
cur.execute(f"SELECT * from user where username='{data}'")
profiledata = cur.fetchone()


def save_profile():

    f = fullname_en.get()
    e = email_en.get()
    g = gender_var.get()
    dob = dob_en.get_date()

    cur.execute(f"UPDATE user SET full_name='{f}', email='{e}', gender='{g}', date_of_birth='{dob}' WHERE sno={profiledata[0]} AND username='{profiledata[1]}'")
    conn.commit()

    root.quit()
    root.destroy()
    os.system("python Main/dig_update_profile_page.py")
def openMainFile(filenm):
    root.quit()
    root.destroy()
    os.system(f"python Main/{filenm}")



top_frame = customtkinter.CTkFrame(master=root, width=int(wow * 0.8), height=75, corner_radius=0,fg_color="#f2f2f2")
top_frame.pack(side="top")
logo_image = customtkinter.CTkImage(light_image=Image.open("./images/logo.png"), dark_image=Image.open("./images/logo.png"), size=(50, 48.4))
l1 = customtkinter.CTkLabel(master=top_frame, image=logo_image, text="")
l1.place(anchor=tkinter.NW, x=20, y=14)


menu_image = customtkinter.CTkImage(light_image=Image.open("./images/menu.png"), dark_image=Image.open("./images/menu.png"), size=(40, 40))
profile = customtkinter.CTkImage(light_image=Image.open("./images/profile.png"), dark_image=Image.open("./images/profile.png"), size=(40, 40))
logout = customtkinter.CTkImage(light_image=Image.open("./images/logout.png"), dark_image=Image.open("./images/logout.png"), size=(40, 40))
create = customtkinter.CTkImage(light_image=Image.open("./images/create.png"), dark_image=Image.open("./images/create.png"), size=(40, 40))
options = [profile, logout, create]

def toggle_dropdown():
    dropdown_menu.withdraw() if dropdown_menu.winfo_viewable() else position_dropdown()

def select_option(path):
    dropdown_menu.withdraw()
    if path == create:
        openMainFile("dig_create_post_page.py")
    elif path == profile:
        openMainFile("dig_update_profile_page.py")
    elif path == logout:
        root.quit()
        root.destroy()
        os.remove("Main/logs/log.bkl")
        os.system("python Dlogin.py")
    else:
        print("Option selected:", path)

def position_dropdown():
    x = menu.winfo_rootx()
    y = menu.winfo_rooty() + menu.winfo_height()
    dropdown_menu.geometry(f"+{x}+{y}")
    dropdown_menu.deiconify()
def edit_position_dropdown():
    x = edit_btn.winfo_rootx()
    y = edit_btn.winfo_rooty() + menu.winfo_height()
    edit_dropdown_menu.geometry(f"+{x}+{y}")
    edit_dropdown_menu.deiconify()

menu = customtkinter.CTkButton(top_frame, image=menu_image, text="", command=toggle_dropdown, width=20, hover=False, fg_color="#f2f2f2")
menu.place(relx=0.9, anchor=tkinter.NW, y=14)

dropdown_menu = tkinter.Toplevel(root,bg="#f2f2f2")
dropdown_menu.overrideredirect(True)
dropdown_menu.withdraw()

for img in options:
    option_button = customtkinter.CTkButton(dropdown_menu, image=img, text="", compound="left", command=lambda img=img: select_option(img), width=20, hover=False, fg_color="#f2f2f2")
    option_button.pack(fill="x", anchor="w")



side_frame = customtkinter.CTkFrame(master=root, height=int(how * 0.55), width=int(wow * 0.15), fg_color="#f2f2f2")
side_frame.pack(side="left")

home_img = customtkinter.CTkImage(light_image=Image.open("./images/home.png"), dark_image=Image.open("./images/home.png"), size=(20, 20))
people_img = customtkinter.CTkImage(light_image=Image.open("./images/people.png"), dark_image=Image.open("./images/people.png"), size=(20, 20))
help_img = customtkinter.CTkImage(light_image=Image.open("./images/help.png"), dark_image=Image.open("./images/help.png"), size=(20, 20))
about_img = customtkinter.CTkImage(light_image=Image.open("./images/about.png"), dark_image=Image.open("./images/about.png"), size=(20, 20))

home_btn = customtkinter.CTkButton(master=side_frame, image=home_img,text=" Home ",command=lambda: openMainFile("dig_home_page.py"), border_width=3, corner_radius=25,font=('Century Gothic Bold',12),fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d")
home_btn.place(relx=0.5, anchor=tkinter.CENTER, y=50)
home_btn.bind("<Enter>",lambda event: home_btn.configure(fg_color="#f0989d",text_color="#7c696e",border_width=0))
home_btn.bind("<Leave>",lambda event: home_btn.configure(fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d",border_width=3))

people_btn = customtkinter.CTkButton(master=side_frame,image=people_img,text="People",command=lambda: openMainFile("dig_people.py"), border_width=3, corner_radius=25,font=('Century Gothic Bold',12),fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d")
people_btn.place(relx=0.5, anchor=tkinter.CENTER, y=100)
people_btn.bind("<Enter>",lambda event: people_btn.configure(fg_color="#f0989d",text_color="#7c696e",border_width=0))
people_btn.bind("<Leave>",lambda event: people_btn.configure(fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d",border_width=3))

help_btn = customtkinter.CTkButton(master=side_frame, image=help_img,text=" Help ",command=lambda: openMainFile("dig_help.py"), border_width=3, corner_radius=25,font=('Century Gothic Bold',12),fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d")
help_btn.place(relx=0.5, anchor=tkinter.CENTER, y=150)
help_btn.bind("<Enter>",lambda event: help_btn.configure(fg_color="#f0989d",text_color="#7c696e",border_width=0))
help_btn.bind("<Leave>",lambda event: help_btn.configure(fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d",border_width=3))

about_btn = customtkinter.CTkButton(master=side_frame,image=about_img, text=" About",command=lambda: openMainFile("dig_about.py"), border_width=3, corner_radius=25,font=('Century Gothic Bold',12),fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d")
about_btn.place(relx=0.5, anchor=tkinter.CENTER, y=200)
about_btn.bind("<Enter>",lambda event: about_btn.configure(fg_color="#f0989d",text_color="#7c696e",border_width=0))
about_btn.bind("<Leave>",lambda event: about_btn.configure(fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d",border_width=3))

def edit(slug):
    def save_edit():
        t = title_en.get()
        d = desc_en.get("1.0", "end-1c")
        cur.execute(f"UPDATE post SET title = '{t}', description = '{d}', edited = {True} WHERE slug = {slug} and username = '{data}'")
        conn.commit()
        root.quit()
        root.destroy()
        os.system("python Main/dig_home_page.py")
    if 'edit_post' in globals():
        edit_post.destroy()

    cur.execute(f"SELECT title,description FROM post WHERE slug={slug}")
    info = cur.fetchone()
    edit_post = customtkinter.CTkToplevel(root)
    edit_post.title("Edit Post")
    edit_post.lift()
    edit_post.wm_attributes("-topmost", True)
    title = customtkinter.CTkLabel(master=edit_post, text="Title")
    title.grid(row=0,column=0,padx=3,pady=3)
    title_en = customtkinter.CTkEntry(master=edit_post)
    title_en.grid(row=0,column=1,padx=3,pady=3)
    desc = customtkinter.CTkLabel(master=edit_post, text="Description")
    desc.grid(row=1,column=0,padx=3,pady=3)
    desc_en = customtkinter.CTkTextbox(master=edit_post)
    desc_en.grid(row=1,column=1,padx=3,pady=3)
    save = customtkinter.CTkButton(master=edit_post, text="Save",command=save_edit, border_width=3, corner_radius=25,font=('Century Gothic Bold',12),fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d")
    save.grid(row=2,column=0,columnspan=2,padx=3,pady=3)
    save.bind("<Enter>",lambda event: save.configure(fg_color="#f0989d",text_color="#7c696e",border_width=0))
    save.bind("<Leave>",lambda event: save.configure(fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d",border_width=3))

    title_en.insert(0,info[0])
    desc_en.insert("1.0",info[1])


def deletepost(slug):
    conf = messagebox.askyesno("Post Deletion !","Do you want to delete this post?")
    if conf:
        cur.execute(f"DELETE FROM post WHERE slug = {slug}")
        conn.commit()
        root.quit()
        root.destroy()
        os.system("python Main/dig_home_page.py")
    else:
        return
def deleteaccount():
    conf = messagebox.askyesno("Account Deletion !","Do you want to delete this account?You cannot Undo it.")
    if conf:
        cur.execute(f"DELETE FROM user WHERE username = '{data}'")
        cur.execute(f"DELETE FROM post WHERE username = '{data}'")
        cur.execute(f"DELETE FROM connections WHERE person = '{data}' OR username = '{data}'")
        conn.commit()
        root.quit()
        root.destroy()
        os.system("python Dlogin.py")
    else:
        return
post_frame = customtkinter.CTkScrollableFrame(master=root, height=int(how * 0.55), width=int(wow * 0.55), fg_color="#f2f2f2")
post_frame.pack(side='right')
userdetaillabel = customtkinter.CTkLabel(master=post_frame, text=f"User Details",font=("Century Gothic Bold",30))
userdetaillabel.pack(anchor="w",pady=5)
user_frame = customtkinter.CTkFrame(master=post_frame, height=int(how * 0.30), width=int(wow * 0.55), fg_color="#ebebeb")
user_frame.pack(fill="both")



def edit_profile():
    global username_en, fullname_en, email_en, gender_var, dob_en
    username.grid_forget()
    fullname.grid_forget()
    email.grid_forget()
    gender.grid_forget()
    dateofbirth.grid_forget()
    edit_profile_btn.grid_forget()
        
    fullname_en = customtkinter.CTkEntry(master=user_frame, placeholder_text="Full Name",font=("Century Gothic",20),width=300,corner_radius=25)
    fullname_en.insert(0, profiledata[3])
    fullname_en.grid(row=0,column=0,padx=3,pady=3)
    
    email_en = customtkinter.CTkEntry(master=user_frame, placeholder_text="Email",font=("Century Gothic",20),width=300,corner_radius=25)
    email_en.insert(0, profiledata[4])
    email_en.grid(row=1,column=0,padx=3,pady=3)
    
    gender_var = tkinter.StringVar(value=profiledata[5])
    gender_male = customtkinter.CTkRadioButton(master=user_frame, text="Male", variable=gender_var, value="M")
    gender_male.grid(row=2,column=0,padx=3,pady=3)
    gender_female = customtkinter.CTkRadioButton(master=user_frame, text="Female", variable=gender_var, value="F")
    gender_female.grid(row=3,column=0,padx=3,pady=3)
    date = str(profiledata[6]).split("-")
    try:
        dob_en = DateEntry(master=user_frame,year=int(date[0]),month=int(date[1]),day=int(date[2]))
        dob_en.grid(row=4,column=0,padx=3,pady=3)
    except:
        dob_en = DateEntry(master=user_frame)
        dob_en.grid(row=4,column=0,padx=3,pady=3)
    save_btn = customtkinter.CTkButton(master=user_frame,text="Save", command=save_profile, border_width=3, corner_radius=25,font=('Century Gothic Bold',12),fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d")
    save_btn.grid(row=5,column=0,padx=3,pady=3)
    save_btn.bind("<Enter>",lambda event: save_btn.configure(fg_color="#7c696e",text_color="#f2f2f2",border_width=0))
    save_btn.bind("<Leave>",lambda event: save_btn.configure(fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d",border_width=3))
    delete_account = customtkinter.CTkButton(user_frame, text="Delete Account",command=deleteaccount, width=20, hover=False,font=('Century Gothic Bold',15),text_color="#f0989d",fg_color="#f2f2f2")
    delete_account.grid(row=5,column=1,padx=3,pady=3)
username = customtkinter.CTkLabel(master=user_frame, text=f"Username: {profiledata[1]}",font=("Century Gothic",20))
username.grid(row=0,column=0,padx=3,pady=3)
fullname = customtkinter.CTkLabel(master=user_frame, text=f"Full Name: {profiledata[3]}",font=("Century Gothic",20))
fullname.grid(row=1,column=0,padx=3,pady=3)
email = customtkinter.CTkLabel(master=user_frame, text=f"Email: {profiledata[4]}",font=("Century Gothic",20))
email.grid(row=2,column=0,padx=3,pady=3)
gender = customtkinter.CTkLabel(master=user_frame, text=f"Gender: {profiledata[5]}",font=("Century Gothic",20))
gender.grid(row=3,column=0,padx=3,pady=3)
dateofbirth = customtkinter.CTkLabel(master=user_frame, text=f"Date of Birth: {profiledata[6]}",font=("Century Gothic",20))
dateofbirth.grid(row=4,column=0,padx=3,pady=3)


edit_profile_btn = customtkinter.CTkButton(master=user_frame,text="Edit Profile", command=edit_profile, border_width=3, corner_radius=25,font=('Century Gothic Bold',12),fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d")
edit_profile_btn.grid(row=5,column=0,padx=3,pady=3)
edit_profile_btn.bind("<Enter>",lambda event: edit_profile_btn.configure(fg_color="#7c696e",text_color="#f2f2f2",border_width=0))
edit_profile_btn.bind("<Leave>",lambda event: edit_profile_btn.configure(fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d",border_width=3))

friends = customtkinter.CTkLabel(master=post_frame, text=f"Your Friends",font=("Century Gothic Bold",30))
friends.pack(anchor="w",pady=5)
people_frame = customtkinter.CTkFrame(master=post_frame, width=int(wow * 0.55), fg_color="#ebebeb")
people_frame.pack(fill="x")
def removefriend(user):
    cur.execute(f"DELETE FROM connections WHERE person='{user}'")
    conn.commit()
    openMainFile('dig_update_profile_page.py')

def display_people(peoples):
    for i in peoples:
        cur.execute(f'SELECT username,full_name FROM user WHERE username="{i[0]}"')   
        friend = cur.fetchone()
        peoples = customtkinter.CTkFrame(master=people_frame,fg_color="white",height=5)
        peoples.pack(fill="both",padx=5,pady=5)
        username = customtkinter.CTkLabel(master=peoples,text=f"@{friend[0]}",font=("Century Gothic Bold",24))
        username.grid(row=0,column=0,padx=10,pady=10)
        fullname = customtkinter.CTkLabel(master=peoples,text=f"~{friend[1]}",font=("Century Gothic ",12))
        fullname.grid(row=1,column=0)
        remove = customtkinter.CTkButton(master=peoples, text="Remove Friend",command=lambda i=i:removefriend(i[0]),hover=False, border_width=3, corner_radius=25,font=('Century Gothic Bold',12),fg_color="#f2f2f2",text_color="#f0989d",border_color="#f0989d")
        remove.place(relx=0.8, anchor=tkinter.CENTER, rely=0.5)
cur.execute(f"SELECT person FROM connections where username='{data}'")
allUsers = cur.fetchall()
display_people(allUsers)

postlablel = customtkinter.CTkLabel(master=post_frame, text=f"Your Posts",font=("Century Gothic Bold",30))
postlablel.pack(anchor="w",pady=5)
def display_posts(posts):
    global edit_btn,edit_dropdown_menu
    for i in posts:
        post = customtkinter.CTkFrame(master=post_frame, fg_color="#f2f2f2")
        post.pack(pady=5, fill="both")
        if i[1] == data:
            user = "You"
            ver_menu_image = customtkinter.CTkImage(light_image=Image.open("./images/ver_menu.png"),
                                                    dark_image=Image.open("./images/ver_menu.png"), size=(20, 20))

            edit_btn = customtkinter.CTkButton(post, image=ver_menu_image, text="", width=20, hover=False,
                                               fg_color="#f2f2f2")
            edit_btn.place(relx=0.9, anchor=tkinter.NW, y=14)

            # Create a new dropdown menu for each post
            edit_dropdown_menu = tkinter.Toplevel(root)
            edit_dropdown_menu.overrideredirect(True)
            edit_dropdown_menu.withdraw()

            def toggle_edit_dropdown(btn=edit_btn, menu=edit_dropdown_menu):
                x = btn.winfo_rootx()
                y = btn.winfo_rooty() + btn.winfo_height()
                menu.geometry(f"+{x-30}+{y}")
                menu.deiconify() if not menu.winfo_viewable() else menu.withdraw()

            edit_btn.configure(command=lambda b=edit_btn, m=edit_dropdown_menu: toggle_edit_dropdown(b, m))

            ed_image = customtkinter.CTkImage(light_image=Image.open("./images/edit.png"),
                                                    dark_image=Image.open("./images/edit.png"), size=(20, 20))
            # Add options to the dropdown menu
            edit_option_button = customtkinter.CTkButton(edit_dropdown_menu,image=ed_image, text="    Edit ",compound="left",
                                                         command=lambda i=i: edit(i[0]), width=20, hover=False,font=('Century Gothic Bold',15),
                                                         text_color="#7c696e",fg_color="#f2f2f2")
            edit_option_button.pack(fill="x", anchor="w")

            del_image = customtkinter.CTkImage(light_image=Image.open("./images/delete.png"),
                                                    dark_image=Image.open("./images/delete.png"), size=(20, 20))
            delete_option_button = customtkinter.CTkButton(edit_dropdown_menu,image=del_image, text="Delete",compound="left",
                                                           command=lambda i=i: deletepost(i[0]), width=20, hover=False,font=('Century Gothic Bold',15),
                                                           text_color="#f0989d",fg_color="#f2f2f2")
            delete_option_button.pack(fill="x", anchor="w")

        else:
            user = f"@{i[1]}"
        username = customtkinter.CTkLabel(master=post, text=f"{user}", font=("Century Gothic Italic", 15),
                                          text_color="#7c696e")
        username.grid(row=0, column=0, sticky="W")
        if i[2] == True:
            is_edited = customtkinter.CTkLabel(master=post, text=" • edited", font=("Century Gothic", 15),
                                               text_color="#f0989d")
            is_edited.grid(row=0, column=1, sticky="W")
        title = customtkinter.CTkLabel(master=post, text=f"{i[3]}", font=("Century Gothic Bold", 25),
                                       text_color="#0c0b0c")
        title.grid(row=1, columnspan=3, column=0, sticky="W")
        desc = customtkinter.CTkLabel(master=post, text=f"{i[4]}", font=("Century Gothic", 15),
                                      text_color="#0c0b0c", justify="left")
        desc.grid(row=3, column=0, sticky="W")
        time = customtkinter.CTkLabel(master=post, text=f"-{i[5]}", font=("Century Gothic", 10),
                                      text_color="#0c0b0c")
        time.grid(row=4, column=0, sticky="W")

        customtkinter.CTkLabel(master=post_frame, text="─" * 400).pack()

cur.execute(f"SELECT * FROM post WHERE username = '{data}'")
search_results = cur.fetchall()[::-1]
display_posts(search_results)

root.mainloop()

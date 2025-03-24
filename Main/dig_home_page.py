import customtkinter
import tkinter
from PIL import Image
import pickle
import mysql.connector as ms
import os
from tkinter import messagebox
root = customtkinter.CTk()
customtkinter.set_appearance_mode("Light")
wow = root.winfo_screenwidth()
how = root.winfo_screenheight()

x = int((wow * 0.2) / 2)
y = int((how * 0.2) / 2)
root.geometry(f'{int(wow * 0.8)}x{int(how * 0.8)}+{x}+{y}')
root.title('Home | Dig')
root.resizable(False, False)
root.protocol("WM_DELETE_WINDOW", quit)
root.config(bg="#f2f2f2")

with open("Main/logs/log.bkl", 'rb') as f:
    data = pickle.load(f)[0]
conn = ms.connect(host="localhost", user="root", database="digbydhawal")
cur = conn.cursor()

def openMainFile(filenm):
    root.quit()
    root.destroy()
    os.system(f"python Main/{filenm}")

def search_posts(x=0):
    search_term = search.get()
    cur.execute(f"SELECT * FROM post WHERE title LIKE '%{search_term}%'")
    search_results = cur.fetchall()[::-1]
    display_posts(search_results)

top_frame = customtkinter.CTkFrame(master=root, width=int(wow * 0.8), height=75, corner_radius=0,fg_color="#f2f2f2")
top_frame.pack(side="top")
logo_image = customtkinter.CTkImage(light_image=Image.open("./images/logo.png"), dark_image=Image.open("./images/logo.png"), size=(50, 48.4))
l1 = customtkinter.CTkLabel(master=top_frame, image=logo_image, text="")
l1.place(anchor=tkinter.NW, x=20, y=14)

search_frame = customtkinter.CTkFrame(master=top_frame, width=int(wow * 0.5),fg_color="#f2f2f2",border_width=0)
search_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
search = customtkinter.CTkEntry(master=search_frame, placeholder_text="Search posts ...", font=("Century Gothic", 15),corner_radius=25, width=500, height=40)
search.grid(row=0,column=0)
search.bind("<Return>",search_posts)
search_icon = customtkinter.CTkImage(light_image=Image.open("./images/search.png"), dark_image=Image.open("./images/search.png"), size=(30, 30))
search_button = customtkinter.CTkButton(master=search_frame, text="", image=search_icon, width=30, corner_radius=25,fg_color="#f0989d",hover=0, command=search_posts)
search_button.grid(row=0, column=1)

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
post_frame = customtkinter.CTkScrollableFrame(master=root, height=int(how * 0.55), width=int(wow * 0.55), fg_color="#f2f2f2")
post_frame.pack(side='right')
def display_posts(posts):
    global edit_btn,edit_dropdown_menu
    for widget in post_frame.winfo_children():
        widget.destroy()
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

cur.execute(f"SELECT * FROM post")
search_results = cur.fetchall()[::-1]
display_posts(search_results)

root.mainloop()
# Dprogressbar page
from tkinter import *
from tkinter import ttk
import mysql.connector as ms
from tkinter import messagebox
import os 

root = Tk()
x = int((root.winfo_screenwidth() - 800) / 2)
y = int((root.winfo_screenheight() - 200) / 2)
root.overrideredirect(True)
root.geometry(f'800x200+{x}+{y}')

root.wm_attributes("-topmost",True)
root.lift()
root.wm_attributes("-topmost",True)
root.wm_attributes("-disabled",True)
root.wm_attributes("-transparentcolor","white")

img = PhotoImage(file="images/progressbar_banner.png")
main_pic = Label(image=img,bg='white',borderwidth=0)
main_pic.place(x=0,y=0)
loading_title = Label(root, text="Loading...",font=('Century Gothic',20),fg='#f2f2f2')
loading_title.place(x=325, y=50)
loading_number = Label(root, text="0%",font=('Century Gothic',12),fg='#f2f2f2')
loading_number.place(x=365, y=125)
loading_txt = Label(root, text="___Establishing connection ...___",font=('Century Gothic',12),fg='#f2f2f2')
loading_txt.place(x=270, y=150)


conn = cur = NONE



def startbar():
    import time
    bar_running = True  
    
    try:
        for i in range(101):
            if not bar_running:  
                break

            bar['value'] = i
            time.sleep(.01)
            ss = str(i) + "%"
            loading_number.config(text=ss)
            root.update_idletasks()

            if i == 20:
                try:
                    conn = ms.connect(host="localhost", user="root")
                    cur = conn.cursor()
                    loading_txt['text'] = "Detecting presence of database ..."
                except:
                    messagebox.showwarning("Connection failed!", "Check your connection")
                    quit()
            elif i == 40:
                try:
                    cur.execute('CREATE DATABASE IF NOT EXISTS digbydhawal')
                    cur.execute('USE digbydhawal')
                    loading_txt['text'] = "Initializing user table ..."
                except:
                    messagebox.showwarning("Database issue", "There is a problem with the database.")
                    quit()
            elif i == 60:
                try:
                    cur.execute('CREATE TABLE IF NOT EXISTS user(sno INT NOT NULL AUTO_INCREMENT, username VARCHAR(50), password VARCHAR(50), full_name VARCHAR(50), email VARCHAR(50), gender VARCHAR(1), PRIMARY KEY(sno));')
                    conn.commit()
                    loading_txt['text'] = "Creating admin access ..."
                except:
                    messagebox.showwarning("Table issue", "There is a problem with the user table.")
                    quit()
            elif i == 80:
                try:
                    cur.execute('SELECT COUNT(*) FROM user WHERE username="admin" AND password="admin"')
                    count = cur.fetchall()
                    if count[0][0] == 0:
                        cur.execute('INSERT INTO user(username, password) VALUES("admin", "admin")')
                        conn.commit()
                except:
                    messagebox.showwarning("Admin issue", "There is a problem with the admin setup.")
                    quit()

            red = int(240 - (i * 0.91))
            green = int(153 - (i * 0.13))
            blue = int(157 - (i * 0.14))
            color = f'#{red:02x}{green:02x}{blue:02x}'
            style.configure("custom.Horizontal.TProgressbar", background=color)
            loading_txt['fg'] = loading_number['fg'] = loading_title['fg'] = color

            if i % 7 == 0:
                loading_txt['fg'] = loading_number['fg'] = '#f2f2f2'
        
        time.sleep(0.3)
        conn.commit()
        conn.close()

    except Exception as e:
        print("Error:", e)

    finally:
        if bar_running: 
            root.quit()

def on_close():
    global bar_running
    bar_running = False
    root.quit()

root.protocol("WM_DELETE_WINDOW", on_close)

style = ttk.Style()
style.theme_use('default')
style.configure("custom.Horizontal.TProgressbar", troughcolor='#eefefe', background='#ff0000')

bar = ttk.Progressbar(root, length=750, value=0, mode='determinate', style="custom.Horizontal.TProgressbar")
bar.place(x=20, y=100)

root.after(700, startbar)

root.mainloop()

root.destroy()


try:
    os.system('python Dwelcomescreen.py')
except Exception as e:
    print("error importing Dwelcome screen >>> ",e)
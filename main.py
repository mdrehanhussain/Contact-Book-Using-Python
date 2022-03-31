import time
import tkinter as tk
from tkinter import ttk
import os
from tkinter import messagebox
#import/
app = tk.Tk()           #starter
#config
app.title("Contact Book")

#Variables
# h1_n = "S/N"
h2_n = "Name"
h3_n = "Job"
h4_n = "Email"
#Code:
#Header
# tk.Label(app, text=h1_n).grid(row=1,column=1)
tk.Label(app, text=h2_n).grid(row=1,column=2)
tk.Label(app, text="     ").grid(row=1,column=3)
tk.Label(app, text=h3_n).grid(row=1,column=4)
tk.Label(app, text="     ").grid(row=1,column=5)
tk.Label(app, text=h4_n).grid(row=1,column=6)
# with open("current_number.txt") as file:
#     ff = file.read()
ff = len(os.listdir("contacts\\"))
for x in range(int(ff)):
    with open("contacts\\" + os.listdir("contacts\\")[x]) as fff:
        contact_info = fff.readlines(0)
        contact_name = contact_info[0]
        contact_job = contact_info[1]
        contact_email = contact_info[2]

    #-----------
    # tk.Label(app,text=x+1).grid(row=x+10, column=1)
    contact_n = os.listdir("contacts\\")[x]
    tk.Label(app, text=contact_name).grid(row=x+2,column=2)
    tk.Label(app, text="     ").grid(row=x+2, column=3)
    tk.Label(app, text=contact_job).grid(row=x+2,column=4)
    tk.Label(app, text="     ").grid(row=x + 2, column=3)
    tk.Label(app, text=contact_email).grid(row=x + 2, column=6)
#funtions

def add():
    add1 = tk.Tk()
    tk.Label(add1, text="Name:").grid(row=1, column=1)
    name = tk.Entry(add1)
    tk.Label(add1, text="Job:").grid(row=2, column=1)
    job = tk.Entry(add1)
    tk.Label(add1, text="Email:").grid(row=3, column=1)
    email = tk.Entry(add1)
    name.grid(row=1, column=2)
    job.grid(row=2, column=2)
    email.grid(row=3, column=2)
    def added():
        name1 = name.get()
        job1 = job.get()
        email1 = email.get()
        with open(f"Contacts\\{name1}.txt", "w") as file:
            file.write(f"{name1}\n{job1}\n{email1}")
        add1.destroy()
        messagebox.showwarning("Reload", "Reload This Program To See Changes")
        # with open("main.py") as mm:
        #     mmm = mm.read()
        #     app.destroy()
        #     exec(mmm)

    tk.Button(add1, text="add", command=added).grid(row=4)
    add1.mainloop()
def delete():
    delete1 = tk.Tk()
    tk.Label(delete1, text="Enter Name:").grid(row=1, column=1)
    naa = tk.Entry(delete1)
    naa.grid(row=1, column=2)
    def deleted():
        name = naa.get()
        os.remove(f"Contacts\\{name}.txt")
        delete1.destroy()
        messagebox.showwarning("Reload", "Reload This Program To See Changes")

    tk.Button(delete1, text="Delete", foreground="red", command=deleted).grid(row=2, column=1)
    delete1.mainloop()

#buttons
tk.Button(app, text="Add", command=add).grid(row=1,column=7)
tk.Button(app, text="Delete", command=delete).grid(row=1,column=9)

app.mainloop()          #Ender
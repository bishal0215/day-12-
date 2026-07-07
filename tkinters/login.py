#login form in  tkinteres python of webpage 
import tkinter as tk
root=tk.Tk()
root.geometry("300x200")
root.title("Login Form")
tk.Label(root, text="Username"). grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Password"). grid(row=1,column=0, padx=10, pady=10)

username_entry=tk.Entry(root)
password_entry=tk.Entry(root, show="*")
username_entry.grid(row=0,column=1, padx=10, pady=10)
password_entry.grid(row=1, column=1,padx=10,pady=10)

def login():
    print("Username:", username_entry.get())
    print("Password:", password_entry.get())
tk.Button(root, text="Login", command=login).grid(row=2, column=0, columnspan=2, pady=10)
root .mainloop()
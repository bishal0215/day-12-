#its for gui 
#it let you build real window buttom and forms - not just text outout in a terminal 
import tkinter as tk 
'''
root = tk.Tk()
root.title("My first app")
root.mainloop()
=============
count = 0 
def on_click():
    global count #its due to use outside of function 
    count +=1
    label.config(text=f"Click:{count}")

root = tk.Tk()
root.title("click counter")
label = tk.Label(root, text="clicks: O", font=("Arial",16))
label.pack(pady=20)
tk.Button(root, text="click me", command=on_click).pack(pady=10)

root.mainloop()
=========

root = tk.Tk()
root.title("my first app")


label = tk.Label(root, text="hello my name is don", font=("Arial",16))
label.pack(pady=20)

root.geometry("400x300")

root.mainloop()
================
'''
root = tk.Tk()
root.title("Personal Info Card")
 
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root).grid(row=0, column=1, padx=10, pady=5)
tk.Label(root, text="Name:")
tk.Entry(root)

 
root.mainloop()
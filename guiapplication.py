#its for gui 
#it let you build real window buttom and forms - not just text outout in a terminal 
import tkinter as tk 
'''
root = tk.Tk()
root.title("My first app")
root.mainloop()
'''
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
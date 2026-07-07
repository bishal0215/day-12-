#simple calculator using tkinter
import tkinter as tk
root=tk.Tk()
root.title("Calculator")
entry=tk.Entry(root,font=("Arial",18),width=15,justify="right")
entry.grid(row=0,column=0, columnspan=4, padx=5, pady=5)

def click(char):
    entry.insert(tk.END,char)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result= eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END,result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END,"Error")
buttons=[
    ('7',1,0),('8',1,1),('9',1,2),('/' ,1,3),
    ('4',2,0),('5',2,1),('6',2,2),('*' ,2,3),
    ('1',3,0),('2',3,1),('3',3,2),('-' ,3,3),
    ('0',4,0),('.' ,4,1),('C' ,4,2),('+' ,4,3),
    ('=' ,5,0,4)]
row,col=1,0
for button in buttons:
    if len(button)==3:
        tk.Button(root,text=button[0],width=5,height=2,font=("Arial",14),command=lambda char=button[0]:click(char)).grid(row=button[1],column=button[2], padx=5, pady=5)
    else:
        tk.Button(root,text=button[0],width=22,height=2,font=("Arial",14),command=calculate).grid(row=button[1],column=button[2], columnspan=button[3], padx=5, pady=5)

tk.Button(root,text='C',width=5,height=2,font=("Arial",14),command=clear).grid(row=4,column=2, padx=5, pady=5)
root.mainloop()

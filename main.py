from tkinter import *

from random import randint


#Geometry

root =Tk()
root.title('Calculator')
root.config(bg="black")
root.resizable(False, False)
img = PhotoImage(file='logo.png')
root.iconphoto(False, img)



# Entry element

ent = Entry(font=('Arial', 20),
      bg='black', 
      fg='white',
      justify=RIGHT
      )
ent.grid(row=0, 
            column=0, 
            columnspan=4,
            padx=3,
            pady=3)
      
#Main functions

def ins_val(v):
    ent.insert(END, v)
    
def result():
    res = eval(ent.get())
    ent.delete(0, END)
    ent.insert(END, res)
    
def clear():
    ent.delete(0, END)
    
def delete():
    ent.delete(len(ent.get())-1, END)
    
    



buttons = [[],
           ['', '', '%','/'],
            ['7','8','9','//'],
           ['4','5','6','+'],
           ['1','2','3','-'],
           ['.','0','/']
]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        btn = Button(text=buttons[i][j], 
               bg='orange',
               fg='white',
               font=('Arial', 15),
               width=5,
               height=2,
               command=lambda val = buttons[i][j]: ins_val(val)
               ).grid(column=j, row=i, 
                              padx=1, pady=1,
                              sticky='wens')
               
               
Button(text='=', 
               bg='orange',
               fg='white',
               font=('Arial', 15),
               width=5,
               height=2,
               command=result).grid(column=3, row=4, 
                              padx=1, pady=1,
                              sticky='wens')

Button(text='C', 
               bg='orange',
               fg='white',
               font=('Arial', 15),
               width=5,
               height=2,
               command=clear).grid(column=1, row=1, 
                              padx=1, pady=1,
                              sticky='wens')
               
Button(text='del', 
               bg='orange',
               fg='white',
               font=('Arial', 15),
               width=5,
               height=2,
               command=delete).grid(column=0, row=1, 
                              padx=1, pady=1,
                              sticky='wens')

        

        

root.mainloop()

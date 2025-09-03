from tkinter import *


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


def create_button(column, row, text, command):
    Button(text=text, 
               bg='orange',
               fg='white',
               font=('Arial', 15),
               width=5,
               height=2,
               command=command).grid(column=column, row=row, 
                              padx=1, pady=1,
                              sticky='wens')
    

def ins_val(v):
    ent.insert(END, v)
    
    
def result():
    try:
        for i in ent.get():
            if i.isalpha():
                ent.delete(0, END)
                ent.insert(END, 'Error.')
                break
        else:
            res = eval(ent.get())
            with open('history.txt', 'a') as file:
                file.write(f'{ent.get()}={res}\n')
            ent.delete(0, END)
            ent.insert(END, res)
    except SyntaxError:
        ent.delete(0, END)
        ent.insert(END, 'Error.')
     
        
def clear():
    ent.delete(0, END)
    
    
def delete():
    ent.delete(len(ent.get())-1, END)
    

def create_new_window():
    wnd = Tk()
    wnd.title('Calculator history')
    wnd.config(bg="black")
    wnd.resizable(False, False)
    

buttons = [['del', 'C', '%','/'],
           ['7', '8', '9', '*'],
           ['4', '5', '6', '+'],
           ['1', '2', '3', '-'],
           ['.', '0', 'History', '=' ]
]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        if buttons[i][j] == 'del':
            create_button(j, i+1, 'del', delete)
        elif buttons[i][j] == 'C':
            create_button(j, i+1, 'C', clear)
        elif buttons[i][j] == '=':
            create_button(j, i+1, '=', result)
        elif buttons[i][j] == 'History':
            create_button(j, i+1, 'History', create_new_window)
        else:
            create_button(j, i+1, buttons[i][j],
                          lambda val = buttons[i][j]: ins_val(val))
               

root.mainloop()

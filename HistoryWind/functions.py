from tkinter import *


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


def create_new_window():
    #New window with history of operations
    
    wnd = Tk()
    wnd.title('Calculator history')
    wnd.config(bg="black")
    wnd.resizable(False, False)
    wnd.geometry()
    
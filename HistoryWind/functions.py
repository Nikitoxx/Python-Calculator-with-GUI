from tkinter import *


def create_new_window():
    
    '''New window with history of operations'''
    
    wnd = Tk()
    wnd.title('Calculator history')
    wnd.config(bg="black")
    wnd.resizable(False, False)
    wnd.geometry()
    
    with open('history.txt', 'r') as file:
        a = file.readlines()
        for i, v in enumerate(a, 1):
            Label(wnd, text=f"{i}. {v}", fg='white', bg='black', font='Arial, 15', anchor='w', justify='left').pack(side='top', fill='x')
        
        
    
    
    
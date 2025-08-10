from tkinter import * 

root =Tk()
root.title('Calculator')
root.config(bg="black")
root.resizable(False, False)





buttons = [['7','8','9','+'],
           ['4','5','6','-'],
           ['1','2','3','*'],
           ['.','0','/','=']
]

for i in range(len(buttons)):
    for j in range(len(buttons)):
        Button(text=buttons[i][j], 
               bg='orange',
               fg='black',
               font='Arial, 15',
               width=5,
               height=2).grid(column=j, row=i)
        

        

root.mainloop()

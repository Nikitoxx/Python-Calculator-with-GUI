from tkinter import * 

root =Tk()
root.title('Calculator')
root.config(bg="black")
root.resizable(False, False)



Entry(font=('Arial', 20)).grid(row=0, column=0, 
                               columnspan=4,
                               padx=3,
                               pady=3)



buttons = [[],
            ['7','8','9','+'],
           ['4','5','6','-'],
           ['1','2','3','*'],
           ['.','0','/','=']
]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        Button(text=buttons[i][j], 
               bg='orange',
               fg='white',
               font=('Arial', 15),
               width=5,
               height=2).grid(column=j, row=i, 
                              padx=1, pady=1,
                              sticky='wens')
        root.grid_columnconfigure(j, minsize=60)
        #root.grid_rowconfigure(i, minsize=60)
        

        

root.mainloop()

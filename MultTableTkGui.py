#Display the multiplication table using GUI

from tkinter import *

main_window = Tk()
main_window.geometry('600x400')
main_window.title("Multiplication Table")
title_font = ("Times",22,'bold')
label_font = ("TimesNewRoman",14)
button_font = ("TimesNewRoman",11,'bold')

label_window = Label(main_window,text = "GUI for printing Multiplication Table",
                     font = title_font,fg = '#32cd32',bg='#ffbf00')
label_window.grid(columnspan=2,pady =10)

def print_table():
    tableof = int(entry_table.get())
    Xplier = int(entry_Xplier.get())
    for i in range(1, Xplier+1):
        message = f'\t{tableof} x {i} = {tableof*i}\n'
        text_box.insert(END, message)

def reset():
    entry_table.delete(0,END)
    entry_Xplier.delete(0,END)
    text_box.delete('1.0',END)
    
    
frame1 = Frame(main_window,highlightbackground="blue",
               highlightthickness=3)
frame1.grid(row = 1, column = 0,padx = 5)
label_table = Label(frame1, text = "Enter the table to be printed",
                    font = label_font)
label_table.grid(row = 0, column = 0,pady =10)
entry_table = Entry(frame1,width = 10)
entry_table.grid(row = 0, column = 1)

label_Xplier = Label(frame1, text = "Enter the END multiplier value",
                     font = label_font)
label_Xplier.grid(row = 1, column = 0,pady=10)
entry_Xplier = Entry(frame1,width = 10)
entry_Xplier.grid(row = 1, column = 1)

print_btn = Button(frame1,text = "PRINT",command = print_table,
                   font =button_font,bg ='#39ff14')
print_btn.grid(columnspan = 2,pady =10)

frame2 = Frame(main_window,highlightbackground="red",
               highlightthickness=3)
frame2.grid(row = 1, column = 1)
label_print = Label(frame2, text = "Multiplication Table",
                    font =button_font)
label_print.grid(columnspan = 2)
text_box = Text(frame2,height=15,width=30)
text_box.grid(columnspan = 2)
reset_btn = Button(main_window,text = "RESET",command = reset,
                   font =button_font,bg='#ffa700')
reset_btn.grid(columnspan = 2,pady =10)

main_window.mainloop()

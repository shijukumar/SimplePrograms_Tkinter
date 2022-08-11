#To print the prime numbers between given values

from tkinter import  *
my_window = Tk()
my_window.geometry('400x270')
my_window.title("Prime Numbers")
title_font = ("Arial",17,'normal')
label_font = ("Times New Roman",14)
button_font = ("Times New Roman",11,'bold')

def print_prime():
    start = int(start_entry.get())
    stop = int(stop_entry.get())
    prime = []
    for n in range (start, stop):
        factors = []
        for i in range(1, n+1):
            rem = n%i
            if rem == 0:
                factors.append(i)
        if len(factors) == 2:
            prime.append(n)
    message = prime
    text_box.insert(END, message)
def reset():
    start_entry.delete(0,END)
    stop_entry.delete(0,END)
    text_box.delete('1.0',END)
    
title_label = Label(text = "Prime numbers between two numbers",font = title_font)
title_label.grid(row = 0,columnspan = 2)
my_frame = Frame(my_window,)
my_frame.grid(row = 1,columnspan = 2)
start_label = Label(my_frame,text = 'Enter the starting number ',font = label_font)
start_label.grid(row = 0,column = 0,pady =10)
start_entry = Entry(my_frame,width = 7,font = label_font)
start_entry.grid(row = 0,column = 1)
stop_label = Label(my_frame,text = 'Enter the ending number ',font = label_font)
stop_label.grid(row = 1,column = 0)
stop_entry = Entry(my_frame,width = 7,font = label_font)
stop_entry.grid(row = 1,column = 1)
print_btn = Button(my_frame,text = "PRINT",command = print_prime,
                   font =button_font,bg ='#39ff14')
print_btn.grid(row = 2,columnspan = 2,pady =5)
text_box = Text(my_frame,height=5,width=37)
text_box.grid(row = 3,columnspan = 2)
reset_btn = Button(my_frame,text = "RESET",command = reset,font =button_font,bg='#ffa700')
reset_btn.grid(row = 4,columnspan = 2,pady =5)

my_window.eval('tk::PlaceWindow . center')
my_window.mainloop()

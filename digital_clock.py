import tkinter as tk
from tkinter import ttk
from tkinter import *
import time
import datetime
from time import strftime
from datetime import datetime
root = Tk()

root.title ("Digital Clock")
root.minsize(950,200)
root.maxsize(1000,200)
#window bg colour
ttk.Style().configure('TFrame', background='black')
backgroundFrame = ttk.Frame(root)
backgroundFrame.place(x=0, y=0, relwidth=1, relheight=1)


#Day-setup
a= datetime.today().strftime('%A')
b= a.upper()
c= b[0:2]
 


#clock-setup
def update_clock():
    string = strftime(' %H: %M: %S  %p')
    label.config(text=string)
    label.after(1000,update_clock)
label = tk.Label(root,font=("Century Gothic",72),background="black",foreground="grey")
label.place(x=270,y=35)
update_clock()

#day
label2 = tk.Label(root,font=("Century Gothic",72),background="black",foreground="grey")
label2.config(text=c+' ~')
label2.place(x=95,y=35)


def labels():
    label3 = tk.Label(root,font=("Century Gothic",8),background="black",foreground="grey",text = "Day")
    label3.place(x=132,y=143)

    label3 = tk.Label(root,font=("Century Gothic",8),background="black",foreground="grey",text = "Hour")
    label3.place(x=332,y=143)

    label3 = tk.Label(root,font=("Century Gothic",8),background="black",foreground="grey",text = "Minutes")
    label3.place(x=450,y=143)

    label3 = tk.Label(root,font=("Century Gothic",8),background="black",foreground="grey",text = "Seconds")
    label3.place(x=620,y=143)

labels()
mainloop()

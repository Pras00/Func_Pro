from tkinter import *
import tkinter.font


root = Tk()
root.title("Temperature Converter")
root.geometry("400x200")

# Font
thefont = tkinter.font.Font(size=15)

# Frame
frame = LabelFrame(root, text = "Temperature Converter", padx = 10, pady = 10)
frame.place(x = 12 , y = 10 )

# judul dan tulisan samadengan 
# judul = Label(frame,text="Temperatur").grid(row = 0, columnspan=3)
sama_dengan = Label(frame, text="-->").grid(row = 1,column = 1)

# Kotas Input
e1 = Entry(frame, width = 15)
e1["font"] = thefont
e1.grid(row = 1, column = 0)
e2 = Entry(frame, width = 15)
e2["font"] = thefont
e2.insert(0, "0")
e2.grid(row = 1, column = 2)

root.mainloop()
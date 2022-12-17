from tkinter import *
from tkinter import ttk
import tkinter.font


window = Tk()
window.title("Temperature Converter")
cnv = Canvas(window, width=300, height=200)
cnv.pack()

cnv.create_line(190, 65, 220, 65)
cnv.create_line(220, 65, 220, 125)
cnv.create_line(220, 125, 190, 125)
cnv.create_line(220, 95, 240, 95)

# Font
thefont = tkinter.font.Font(size=15)

# Judul
judul = Label(window, text="TEMPERATURE CONVERTER", font=("georgia", 11, "bold")).place(x=17, y=13)

# Kotas Input
e1 = Entry(window, width = 15, font=thefont)
e1.place(x= 20, y = 50)
e2 = Entry(window, width = 15, font=thefont)
e2.insert(0, "0")
e2.place(x= 20, y = 110)

# Pilihan Temperatur
pilihan = ["Celcius", "Reamur", "Fahrenheit", "Kelvin"]
box = ttk.Combobox(window, values=pilihan, width= 24)
box.current(0)
box.place(x= 20, y = 80)

box2 = ttk.Combobox(window, values=pilihan, width= 24)
box2.current(1)
box2.place(x= 20, y = 140)

# Tombol Konvert
btn = Button(window, text = "Convert", command=lambda : hasil())
btn.place(x=240, y=83)

# ======================================================================================================================================

# Rumus Konversi Celcius
cel_reamur = lambda x : f"{4/5 * x}° R"
cel_fahrenheit = lambda x : f"{(9/5 * x) + 32}° F"
cel_kelvin = lambda x : f"{x + 273}° K"

# Rumus Konversi Reamur
rea_celcius = lambda x : f"{5/4 * x}° C"
rea_fahrenheit = lambda x : f"{(9/4 * x) + 32}° F"
rea_kelvin = lambda x : f"{(5/4 * x) + 273}° K"

# Rumus Konversi Fahrenheit
fah_celcius = lambda x : f"{5/9 * (x - 32)}° C"
fah_reamur = lambda x : f"{4/9 * (x - 32)}° R"
fah_kelvin = lambda x : f"{(5/9 * (x - 32)) + 273}° K"

# Rumus Konversi Kelvin
kel_celcius = lambda x : f"{x - 273}° C"
kel_reamur = lambda x : f"{4/5 * (x - 273)}° R"
kel_fahrenheit = lambda x : f"{(9/5 * (x - 273)) + 32}° F"

def hasil():
    # Hapus isi kotak2
    e2.delete(0,END)
    
    # Mengambil nilai dari kotak
    kotak1 = box.get()
    kotak2 = box2.get()
    ins = int(e1.get())

    # Menghitung Rumus
    hitungan = []
    def celcius():
        if kotak1 == "Celcius" and kotak2 == "Reamur":
            hitungan.append(cel_reamur(ins))
        elif kotak1 == "Celcius" and kotak2 == "Fahrenheit":
            hitungan.append(cel_fahrenheit(ins))
        elif kotak1 == "Celcius" and kotak2 == "Kelvin":
            hitungan.append(cel_kelvin(ins))
        elif kotak1 == "Celcius" and kotak2 == "Celcius":
            hitungan.append(f"{ins}° C")
        else:
            reamur()

    def reamur():
        if kotak1 == "Reamur" and kotak2 == "Celcius":
            hitungan.append(rea_celcius(ins))
        elif kotak1 == "Reamur" and kotak2 == "Fahrenheit":
            hitungan.append(rea_fahrenheit(ins))
        elif kotak1 == "Reamur" and kotak2 == "Kelvin":
            hitungan.append(rea_kelvin(ins))
        elif kotak1 == "Reamur" and kotak2 == "Reamur":
            hitungan.append(f"{ins}° R")
        else:
            fahrenheit()

    def fahrenheit():
        if kotak1 == "Fahrenheit" and kotak2 == "Celcius":
            hitungan.append(fah_celcius(ins))
        elif kotak1 == "Fahrenheit" and kotak2 == "Reamur":
            hitungan.append(fah_reamur(ins))
        elif kotak1 == "Fahrenheit" and kotak2 == "Kelvin":
            hitungan.append(fah_kelvin(ins))
        elif kotak1 == "Fahrenheit" and kotak2 == "Fahrenheit":
            hitungan.append(f"{ins}° F")
        else:
            kelvin()

    def kelvin():
        if kotak1 == "Kelvin" and kotak2 == "Celcius":
            hitungan.append(kel_celcius(ins))
        elif kotak1 == "Kelvin" and kotak2 == "Reamur":
            hitungan.append(kel_reamur(ins))
        elif kotak1 == "Kelvin" and kotak2 == "Fahrenheit":
            hitungan.append(kel_fahrenheit(ins))
        else:
            hitungan.append(f"{ins}° K")

    # Memanggil Fungsi
    celcius()
    # Menampilkan hasil
    e2.insert(0,hitungan[0])


# Looping Run Program
window.mainloop()
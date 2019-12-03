from tkinter import *

# functions


def slider():
    selection = "Set = " + str(var.get())
    value.config(text=selection)


# main
window = Tk()
window.minsize(450, 600)
window.title("Hello")
window.configure(background="black")


var = DoubleVar()
scale = Scale(window, variable=var)
scale.place(x=25, y=10)

button = Button(window, text="Apply", command=slider)
button.place(x=25, y=120)

value = Label(window)
value.place(x=25, y=150)

canvas = Canvas(window, width=400, height=400)
canvas.place(x=25, y=180)
canvas.create_rectangle((0, 0, 400, 400), fill="#ffffff",
                        width=0)  # rysuję biały prostokąt

# arc_id = canvas.create_arc((0, 0, 50, 25), start=20, extend=30, style=ARC)


# run main loop
window.mainloop()

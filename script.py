from tkinter import *

# key down func


def click():
    entered_text = textentry.get()
    output.delete(0.0, END)
    try:
        answer = my_dictionary[entered_text]
    except:
        answer = "I don't get it"
    output.insert(END, answer)


# main
window = Tk()
window.title("Hello")
window.configure(background="black")

# Photo
photo1 = PhotoImage(file="img.png")
Label(window, image=photo1, bg="black").grid(row=0, column=0, sticky=W)
Label(window, image=photo1, bg="black").grid(row=0, column=1, sticky=W)

# Label
Label(window, text="Write some text", bg="black", fg="white",
      font="none 12 bold").grid(row=1, column=0, sticky=E)

# text entry
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=E)

# submit button
submitbutton = Button(window, text="submit", width=10, command=click)
submitbutton.grid(row=2, column=1, sticky=W)

# Label 2
Label(window, text="Output:", bg="black", fg="white",
      font="none, 16 bold").grid(row=1, column=1, sticky=W)

# Output
output = Text(window, width=30, height=1, wrap=WORD, background="white")
output.grid(row=1, column=1, sticky=E)

# dictionary
my_dictionary = {
    'Hi': 'Hello',
    'hi': 'Hello',
    'Good bye': 'See Ya',
    'good bye': 'See Ya',
}


# run main loop
window.mainloop()

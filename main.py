from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Setting up Main Window
root = Tk()
root.title('Denominations Calculator')
root.configure(bg='light blue')
root.geometry('650x400')

# Adding Image and Labels in the Main Window
upload = Image.open("images.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='light blue')
label.place(x=180, y=20)

label1 = Label(root, text="Hey User! Welcome to Denomination Counter Application.",
               bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

# Function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.configure(bg='light grey')
    top.geometry("600x350+50+50")

    label = Label(top, text="Enter total amount", bg='light grey')
    label.place(x=230, y=50)

    entry = Entry(top)
    entry.place(x=200, y=80)

    lbl = Label(top, text="Here are number of notes for each denomination", bg='light grey')
    lbl.place(x=140, y=170)

    l1 = Label(top, text="2000", bg='light grey')
    l2 = Label(top, text="500",  bg='light grey') 
    l3 = Label(top, text="100",  bg='light grey')

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    def calculator():
        try:
            amount = int(entry.get())
            note2000 = amount // 2000
            amount %= 2000
            note500 = amount // 500
            amount %= 500
            note100 = amount // 100

            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(top, text='Calculate', command=calculator, bg='brown', fg='white')
    btn.place(x=240, y=120)

# Function to show message and call top window
def msg():
    messagebox.showinfo("Alert", "Do you want to calculate the denomination count?")
    topwin()

# Adding Button to the main window
button1 = Button(root,
                 text="Let's get started!",
                 command=msg,
                 bg='brown',
                 fg='white')
button1.place(x=260, y=360)

root.mainloop()

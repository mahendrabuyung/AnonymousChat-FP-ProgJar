import tkinter as tk

HEIGHT = 600
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='green')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

label = tk.Label(frame, text="Anonymous Chat", bg='green',
                 fg='white', font=("normal", 30))
label.pack(fill='both', side='right')
label.place(x=450, y=50)

label1 = tk.Label(frame, text="Select room:", bg='green',
                  fg='white', font=("normal", 30))
label1.pack(fill='both', side='left')
label1.place(x=50, y=120)

button1 = tk.Button(frame, text="1", bg='white',
                    fg='black', font=("normal", 10))
button1.place(x=100, y=200, width=100, height=40)

button2 = tk.Button(frame, text="2", bg='white',
                    fg='black', font=("normal", 10))
button2.place(x=220, y=200, width=100, height=40)

button3 = tk.Button(frame, text="3", bg='white',
                    fg='black', font=("normal", 10))
button3.place(x=340, y=200, width=100, height=40)

button4 = tk.Button(frame, text="4", bg='white',
                    fg='black', font=("normal", 10))
button4.place(x=460, y=200, width=100, height=40)

button5 = tk.Button(frame, text="5", bg='white',
                    fg='black', font=("normal", 10))
button5.place(x=100, y=250, width=100, height=40)

button6 = tk.Button(frame, text="6", bg='white',
                    fg='black', font=("normal", 10))
button6.place(x=220, y=250, width=100, height=40)

button7 = tk.Button(frame, text="7", bg='white',
                    fg='black', font=("normal", 10))
button7.place(x=340, y=250, width=100, height=40)

button8 = tk.Button(frame, text="8", bg='white',
                    fg='black', font=("normal", 10))
button8.place(x=460, y=250, width=100, height=40)

button9 = tk.Button(frame, text="9", bg='white',
                    fg='black', font=("normal", 10))
button9.place(x=100, y=300, width=100, height=40)

button10 = tk.Button(frame, text="10", bg='white',
                     fg='black', font=("normal", 10))
button10.place(x=220, y=300, width=100, height=40)

button11 = tk.Button(frame, text="11", bg='white',
                     fg='black', font=("normal", 10))
button11.place(x=340, y=300, width=100, height=40)

button12 = tk.Button(frame, text="12", bg='white',
                     fg='black', font=("normal", 10))
button12.place(x=460, y=300, width=100, height=40)

label = tk.Label(frame, text="or Create your won room!", bg='green',
                 fg='white', font=("normal", 10))
label.pack(fill='both', side='right')
label.place(x=450, y=450)

buttonRoom = tk.Button(frame, text="Create room!", bg='white',
                       fg='black', font=("normal", 10))
buttonRoom.place(x=500, y=500, width=100, height=40)

root.mainloop()

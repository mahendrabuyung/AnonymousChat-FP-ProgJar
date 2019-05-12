import tkinter as tk

HEIGHT = 600
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='green')
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

button = tk.Button(frame, text="Start Chat!", bg='white',
                   fg='black', font=("normal", 20))
button.pack(side='bottom')
button.place(x=550, y=500, relwidth=0.2, relheight=0.1, relx=0.0, rely=0.0)

label = tk.Label(frame, text="Anonymous Chat", bg='green',
                 fg='white', font=("normal", 50))
label.pack(fill='both', side='left')
label.place(x=50, y=50)

label1 = tk.Label(frame, text="Enjoy the sensation of chatting \nwithout having to register \nan account and login.", bg='green',
                  fg='white', font=("normal", 30), justify='left')
label1.pack(fill='both', side='left')
label1.place(x=50, y=150)

root.mainloop()

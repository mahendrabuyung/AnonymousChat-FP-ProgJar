try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

class Welcome():

    def __init__(self,master):
	
        self.master=master
        self.master.geometry('400x200+100+200')
        self.master.title('Welcome')

        self.label1=tk.Label(self.master,text='Welcome to the wages calculator GUI',fg='red').grid(row=0,column=2)
        self.button1=tk.Button(self.master,text="OK",fg='blue',command=self.gotoWages).grid(row=6,column=2)
        self.button2=tk.Button(self.master,text="QUIT",fg='blue',command=self.finish).grid(row=6,column=3)

    def gotoWages(self):
        root=tk.Tk()
        root.resizable(False, False)
        myGUI=Wages(root)
        self.master.destroy()
		
    def finish(self):
        self.master.destroy()

class Wages():
    def __init__(self, master):
	
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.master=master
        self.master.geometry("352x182")
        self.master.title("Anonymous Chat")
        self.master.configure(background="#31BA7F")
        self.master.configure(highlightbackground="#d9d9d9")
        self.master.configure(highlightcolor="black")

        self.FrameBox = tk.Frame(self.master)
        self.FrameBox.place(relx=0.028, rely=0.055, relheight=0.896
                , relwidth=0.94)
        self.FrameBox.configure(relief='groove')
        self.FrameBox.configure(borderwidth="2")
        self.FrameBox.configure(relief="groove")
        self.FrameBox.configure(background="#31BA7F")
        self.FrameBox.configure(highlightbackground="#d9d9d9")
        self.FrameBox.configure(highlightcolor="black")
        self.FrameBox.configure(width=325)

        self.Lets_Chat = tk.Button(self.FrameBox)
        self.Lets_Chat.place(relx=0.393, rely=0.736, height=24, width=87)
        self.Lets_Chat.configure(activebackground="#31BA7F")
        self.Lets_Chat.configure(activeforeground="#ffffff")
        self.Lets_Chat.configure(background="#31BA7F")
        self.Lets_Chat.configure(disabledforeground="#a3a3a3")
        self.Lets_Chat.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Lets_Chat.configure(foreground="#ffffff")
        self.Lets_Chat.configure(highlightbackground="#d9d9d9")
        self.Lets_Chat.configure(highlightcolor="#ffffff")
        self.Lets_Chat.configure(pady="0")
        self.Lets_Chat.configure(text='''Let's Chat''')

        self.Kembali = tk.Button(self.FrameBox, command=self.finish)
        self.Kembali.place(relx=0.695, rely=0.736, height=24, width=88)
        self.Kembali.configure(activebackground="#31BA7F")
        self.Kembali.configure(activeforeground="#ffffff")
        self.Kembali.configure(background="#31BA7F")
        self.Kembali.configure(disabledforeground="#a3a3a3")
        self.Kembali.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Kembali.configure(foreground="#ffffff")
        self.Kembali.configure(highlightbackground="#d9d9d9")
        self.Kembali.configure(highlightcolor="#ffffff")
        self.Kembali.configure(pady="0")
        self.Kembali.configure(text='''Keluar''')

        self.txtUsername = tk.Entry(self.FrameBox)
        self.txtUsername.place(relx=0.045, rely=0.399, height=30, relwidth=0.912)

        self.txtUsername.configure(background="#ffffffffffff")
        self.txtUsername.configure(disabledforeground="#a3a3a3")
        self.txtUsername.configure(font="TkFixedFont")
        self.txtUsername.configure(foreground="#000000")
        self.txtUsername.configure(highlightbackground="#d9d9d9")
        self.txtUsername.configure(highlightcolor="black")
        self.txtUsername.configure(insertbackground="black")
        self.txtUsername.configure(justify='center')
        self.txtUsername.configure(selectbackground="#c4c4c4")
        self.txtUsername.configure(selectforeground="black")

        self.Label1 = tk.Label(self.FrameBox)
        self.Label1.place(relx=0.03, rely=0.123, height=34, width=173)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#31BA7F")
        self.Label1.configure(disabledforeground="#31BA7F")
        self.Label1.configure(font="-family {Segoe UI} -size 15 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Take a Username:''')

    def finish(self):
        self.master.destroy()

def main():
    root=tk.Tk()
    myGUIWelcome=Welcome(root)
    root.mainloop()

if __name__ == '__main__':
    main()
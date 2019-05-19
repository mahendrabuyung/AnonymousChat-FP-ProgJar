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
	
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.master=master
        self.master.geometry("518x311+396+112")
        self.master.title("Anonymous Chat")
        self.master.configure(background="#31BA7F")

        self.Label1 = tk.Label(self.master)
        self.Label1.place(relx=0.058, rely=0.161, height=56, width=303)
        self.Label1.configure(activebackground="#31BA7F")
        self.Label1.configure(activeforeground="#ffffff")
        self.Label1.configure(background="#31BA7F")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI} -size 28 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''Anonymous Chat''')
        self.Label1.configure(width=303)

        self.Label2 = tk.Label(self.master)
        self.Label2.place(relx=0.058, rely=0.354, height=27, width=218)
        self.Label2.configure(background="#31BA7F")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI} -size 12")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''Enjoy the sensation of chatting''')

        self.Label3 = tk.Label(self.master)
        self.Label3.place(relx=0.058, rely=0.45, height=21, width=184)
        self.Label3.configure(background="#31BA7F")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI} -size 12")
        self.Label3.configure(foreground="#ffffff")
        self.Label3.configure(text='''without having to register''')
        self.Label3.configure(width=184)

        self.Label4 = tk.Label(self.master)
        self.Label4.place(relx=0.058, rely=0.547, height=27, width=153)
        self.Label4.configure(background="#31BA7F")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI} -size 12")
        self.Label4.configure(foreground="#ffffff")
        self.Label4.configure(text='''an account and login.''')
        self.Label4.configure(width=153)

        self.Button1 = tk.Button(self.master, command=self.gotoConn)
        self.Button1.place(relx=0.637, rely=0.707, height=54, width=147)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#ffffff")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 16 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Start Chat!''')
        self.Button1.configure(width=147)

    def gotoConn(self):
        root=tk.Tk()
        root.resizable(False, False)
        GUIConn=Connection(root)
        self.master.destroy()
		
    def finish(self):
        self.master.destroy()

class Connection():

    def __init__(self, master):
	
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.master=master
        self.master.geometry("397x226")
        self.master.title("Anonymous Chat")
        self.master.configure(background="#31BA7F")
        self.master.configure(highlightbackground="#d9d9d9")
        self.master.configure(highlightcolor="black")

        self.FrameBox = tk.Frame(self.master)
        self.FrameBox.place(relx=0.038, rely=0.044, relheight=0.898
                , relwidth=0.935)
        self.FrameBox.configure(relief='groove')
        self.FrameBox.configure(borderwidth="2")
        self.FrameBox.configure(relief="groove")
        self.FrameBox.configure(background="#31BA7F")
        self.FrameBox.configure(highlightbackground="#d9d9d9")
        self.FrameBox.configure(highlightcolor="black")
        self.FrameBox.configure(width=371)

        self.LabelFrameConn = tk.LabelFrame(self.FrameBox)
        self.LabelFrameConn.place(relx=0.027, rely=0.246, relheight=0.714
                , relwidth=0.943)
        self.LabelFrameConn.configure(relief='groove')
        self.LabelFrameConn.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.LabelFrameConn.configure(foreground="#ccfff8")
        self.LabelFrameConn.configure(text='''Connection Info''')
        self.LabelFrameConn.configure(background="#31BA7F")
        self.LabelFrameConn.configure(width=350)

        self.Lets_Chat = tk.Button(self.LabelFrameConn)
        self.Lets_Chat.place(relx=0.429, rely=0.759, height=24, width=87
                , bordermode='ignore')
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

        self.Kembali = tk.Button(self.LabelFrameConn, command=self.backWelcome)
        self.Kembali.place(relx=0.714, rely=0.759, height=24, width=88
                , bordermode='ignore')
        self.Kembali.configure(activebackground="#31BA7F")
        self.Kembali.configure(activeforeground="#ffffff")
        self.Kembali.configure(background="#31BA7F")
        self.Kembali.configure(disabledforeground="#a3a3a3")
        self.Kembali.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.Kembali.configure(foreground="#ffffff")
        self.Kembali.configure(highlightbackground="#d9d9d9")
        self.Kembali.configure(highlightcolor="#ffffff")
        self.Kembali.configure(pady="0")
        self.Kembali.configure(text='''Back''')

        self.Hostname = tk.Label(self.LabelFrameConn)
        self.Hostname.place(relx=0.057, rely=0.138, height=21, width=63
                , bordermode='ignore')
        self.Hostname.configure(activebackground="#31BA7F")
        self.Hostname.configure(activeforeground="#000000")
        self.Hostname.configure(background="#31BA7F")
        self.Hostname.configure(disabledforeground="#a3a3a3")
        self.Hostname.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Hostname.configure(foreground="#ffffff")
        self.Hostname.configure(text='''Hostname''')

        self.port_recv = tk.Label(self.LabelFrameConn)
        self.port_recv.place(relx=0.557, rely=0.345, height=21, width=61
                , bordermode='ignore')
        self.port_recv.configure(activebackground="#f9f9f9")
        self.port_recv.configure(activeforeground="black")
        self.port_recv.configure(background="#31BA7F")
        self.port_recv.configure(disabledforeground="#31BA7F")
        self.port_recv.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.port_recv.configure(foreground="#ffffff")
        self.port_recv.configure(highlightbackground="#d9d9d9")
        self.port_recv.configure(highlightcolor="black")
        self.port_recv.configure(text='''Recv''')

        self.Port = tk.Label(self.LabelFrameConn)
        self.Port.place(relx=0.057, rely=0.345, height=21, width=61
                , bordermode='ignore')
        self.Port.configure(activebackground="#f9f9f9")
        self.Port.configure(activeforeground="#ffffff")
        self.Port.configure(background="#31BA7F")
        self.Port.configure(disabledforeground="#a3a3a3")
        self.Port.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Port.configure(foreground="#ffffff")
        self.Port.configure(highlightbackground="#d9d9d9")
        self.Port.configure(highlightcolor="black")
        self.Port.configure(text='''Port''')

        self.port_send = tk.Label(self.LabelFrameConn)
        self.port_send.place(relx=0.786, rely=0.345, height=21, width=61
                , bordermode='ignore')
        self.port_send.configure(activebackground="#f9f9f9")
        self.port_send.configure(activeforeground="black")
        self.port_send.configure(background="#31BA7F")
        self.port_send.configure(disabledforeground="#a3a3a3")
        self.port_send.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.port_send.configure(foreground="#ffffff")
        self.port_send.configure(highlightbackground="#d9d9d9")
        self.port_send.configure(highlightcolor="black")
        self.port_send.configure(text='''Send''')
        self.port_send.configure(width=61)

        self.hostname_entry = tk.Entry(self.LabelFrameConn)
        self.hostname_entry.place(relx=0.343, rely=0.138, height=20
                , relwidth=0.617, bordermode='ignore')
        self.hostname_entry.configure(background="white")
        self.hostname_entry.configure(disabledforeground="#a3a3a3")
        self.hostname_entry.configure(font="TkFixedFont")
        self.hostname_entry.configure(foreground="#000000")
        self.hostname_entry.configure(insertbackground="black")
        self.hostname_entry.configure(width=214)

        self.ftp_entry = tk.Entry(self.LabelFrameConn)
        self.ftp_entry.place(relx=0.329, rely=0.483, height=20, relwidth=0.177
                , bordermode='ignore')
        self.ftp_entry.configure(background="white")
        self.ftp_entry.configure(disabledforeground="#a3a3a3")
        self.ftp_entry.configure(font="TkFixedFont")
        self.ftp_entry.configure(foreground="#000000")
        self.ftp_entry.configure(highlightbackground="#d9d9d9")
        self.ftp_entry.configure(highlightcolor="black")
        self.ftp_entry.configure(insertbackground="black")
        self.ftp_entry.configure(selectbackground="#c4c4c4")
        self.ftp_entry.configure(selectforeground="black")
        self.ftp_entry.configure(width=64)

        self.port_ftp = tk.Label(self.LabelFrameConn)
        self.port_ftp.place(relx=0.329, rely=0.345, height=21, width=61
                , bordermode='ignore')
        self.port_ftp.configure(activebackground="#f9f9f9")
        self.port_ftp.configure(activeforeground="black")
        self.port_ftp.configure(background="#31BA7F")
        self.port_ftp.configure(disabledforeground="#a3a3a3")
        self.port_ftp.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.port_ftp.configure(foreground="#ffffff")
        self.port_ftp.configure(highlightbackground="#d9d9d9")
        self.port_ftp.configure(highlightcolor="black")
        self.port_ftp.configure(text='''FTP''')

        self.recv_entry = tk.Entry(self.LabelFrameConn)
        self.recv_entry.place(relx=0.557, rely=0.483, height=20, relwidth=0.177
                , bordermode='ignore')
        self.recv_entry.configure(background="white")
        self.recv_entry.configure(disabledforeground="#a3a3a3")
        self.recv_entry.configure(font="TkFixedFont")
        self.recv_entry.configure(foreground="#000000")
        self.recv_entry.configure(highlightbackground="#d9d9d9")
        self.recv_entry.configure(highlightcolor="black")
        self.recv_entry.configure(insertbackground="black")
        self.recv_entry.configure(selectbackground="#c4c4c4")
        self.recv_entry.configure(selectforeground="black")

        self.send_entry = tk.Entry(self.LabelFrameConn)
        self.send_entry.place(relx=0.786, rely=0.483, height=20, relwidth=0.177
                , bordermode='ignore')
        self.send_entry.configure(background="white")
        self.send_entry.configure(disabledforeground="#a3a3a3")
        self.send_entry.configure(font="TkFixedFont")
        self.send_entry.configure(foreground="#000000")
        self.send_entry.configure(highlightbackground="#d9d9d9")
        self.send_entry.configure(highlightcolor="black")
        self.send_entry.configure(insertbackground="black")
        self.send_entry.configure(selectbackground="#c4c4c4")
        self.send_entry.configure(selectforeground="black")

        self.WelcomeAnonChat = tk.Label(self.FrameBox)
        self.WelcomeAnonChat.place(relx=0.013, rely=0.049, height=31, width=354)
        self.WelcomeAnonChat.configure(background="#31BA7F")
        self.WelcomeAnonChat.configure(disabledforeground="#a3a3a3")
        self.WelcomeAnonChat.configure(font="-family {Segoe UI} -size 14 -weight bold")
        self.WelcomeAnonChat.configure(foreground="#ffffff")
        self.WelcomeAnonChat.configure(text='''Welcome to Anonymous Chat''')
        self.WelcomeAnonChat.configure(width=354)

    def backWelcome(self):
        root=tk.Tk()
        root.resizable(False, False)
        GUIWelcome=Welcome(root)
        self.master.destroy()

def main():
    root=tk.Tk()
    myGUIWelcome=Welcome(root)
    root.mainloop()

if __name__ == '__main__':
    main()
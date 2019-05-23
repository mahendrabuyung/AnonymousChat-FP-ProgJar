import sys
import ClientApp as CA
import threading
import Response as Res
import Request as Req
import queue 
import emoji
import emo
import os
import re
from functools import partial

try:
    import Tkinter as tk
    from Tkinter import filedialog
    from Tkinter import *    
except ImportError:
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

txtHost = '127.0.0.1'
txtSend = CA.PORT_SEND
txtRecv = CA.PORT_RECV
txtFTP  = CA.PORT_FTP

message_list = []
message_list_toGroup = []
tab_names = ["public"]
currentlyactivetab = ""


_nonbmp = re.compile(r'[\U00010000-\U0010FFFF]')

def _surrogatepair(match):
    char = match.group()
    assert ord(char) > 0xffff
    encoded = char.encode('utf-16-le')
    return (
        chr(int.from_bytes(encoded[:2], 'little')) + 
        chr(int.from_bytes(encoded[2:], 'little')))

def rendertext(text):
    return _nonbmp.sub(_surrogatepair, emoji.emojize(text))

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

        self.Lets_Chat = tk.Button(self.LabelFrameConn, command=self.openMainWindow)
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

        self.hostname_entry = tk.Entry(self.LabelFrameConn)#, textvariable=txtHost)
        self.hostname_entry.place(relx=0.343, rely=0.138, height=20
                , relwidth=0.617, bordermode='ignore')
        self.hostname_entry.configure(background="white")
        self.hostname_entry.configure(disabledforeground="#a3a3a3")
        self.hostname_entry.configure(font="TkFixedFont")
        self.hostname_entry.configure(foreground="#000000")
        self.hostname_entry.configure(insertbackground="black")
        self.hostname_entry.configure(width=214)
        self.hostname_entry.insert(0,txtHost)
        self.hostname_entry.configure(justify='center')

        self.ftp_entry = tk.Entry(self.LabelFrameConn)#, textvariable=txtFTP)
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
        self.ftp_entry.insert(0,txtFTP)
        self.ftp_entry.configure(justify='center')

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

        self.recv_entry = tk.Entry(self.LabelFrameConn)#, textvariable=txtRecv)
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
        self.recv_entry.insert(0,txtRecv)
        self.recv_entry.configure(justify='center')
		
        self.send_entry = tk.Entry(self.LabelFrameConn)#, textvariable=txtSend)
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
        self.send_entry.insert(0,txtSend)
        self.send_entry.configure(justify='center')
		
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

    def openMainWindow(self):
        global txtHost, txtRecv, txtSend, txtFTP
        txtHost = self.hostname_entry.get()
        txtRecv = self.recv_entry.get()
        txtSend = self.send_entry.get()
        txtFTP = self.ftp_entry.get()
        CA.run(txtHost, int(txtSend), int(txtRecv), int(txtFTP))
        #print (txtHost, txtRecv, txtSend, txtFTP)	
        root=tk.Tk()
        root.resizable(False, False)
        GUIMain=AnonWinMain(root)
        self.master.destroy()

class AnonWinMain:
    def __init__(self,master):
        global my_msg, path_msg
        my_msg = tk.StringVar()
        my_msg.set("Type your messages here.")
        path_msg = tk.StringVar()
        path_msg.set("")

        self.msgcount = 0

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        self.master=master
        self.master.geometry("810x576+394+7")
        self.master.title("Anonymous Chat")
        self.master.configure(background="#31BA7F")

        self.images = (

         tk.PhotoImage("img_close", data='''R0lGODlhDAAMAIQUADIyMjc3Nzk5OT09PT
                 8/P0JCQkVFRU1NTU5OTlFRUVZWVmBgYGF hYWlpaXt7e6CgoLm5ucLCwszMzNbW
                 1v//////////////////////////////////// ///////////yH5BAEKAB8ALA
                 AAAAAMAAwAAAUt4CeOZGmaA5mSyQCIwhCUSwEIxHHW+ fkxBgPiBDwshCWHQfc5
                 KkoNUtRHpYYAADs= '''),

         tk.PhotoImage("img_closeactive", data='''R0lGODlhDAAMAIQcALwuEtIzFL46
                 INY0Fdk2FsQ8IdhAI9pAIttCJNlKLtpLL9pMMMNTP cVTPdpZQOBbQd60rN+1rf
                 Czp+zLxPbMxPLX0vHY0/fY0/rm4vvx8Pvy8fzy8P//////// ///////yH5BAEK
                 AB8ALAAAAAAMAAwAAAVHYLQQZEkukWKuxEgg1EPCcilx24NcHGYWFhx P0zANBE
                 GOhhFYGSocTsax2imDOdNtiez9JszjpEg4EAaA5jlNUEASLFICEgIAOw== '''),

         tk.PhotoImage("img_closepressed", data='''R0lGODlhDAAMAIQeAJ8nD64qELE
                 rELMsEqIyG6cyG7U1HLY2HrY3HrhBKrlCK6pGM7lD LKtHM7pKNL5MNtiViNaon
                 +GqoNSyq9WzrNyyqtuzq+O0que/t+bIwubJw+vJw+vTz+zT z////////yH5BAE
                 KAB8ALAAAAAAMAAwAAAVJIMUMZEkylGKuwzgc0kPCcgl123NcHWYW Fs6Gp2mYB
                 IRgR7MIrAwVDifjWO2WwZzpxkxyfKVCpImMGAeIgQDgVLMHikmCRUpMQgA7 ''')
        )

        self.style.element_create("close", "image", "img_close",
               ("active", "pressed", "!disabled", "img_closepressed"),
               ("active", "alternate", "!disabled",
               "img_closeactive"), border=8, sticky='')

        self.style.layout("ClosetabNotebook", [("ClosetabNotebook.client",
                                     {"sticky": "nswe"})])
        self.style.layout("ClosetabNotebook.Tab", [
            ("ClosetabNotebook.tab",
              { "sticky": "nswe",
                "children": [
                    ("ClosetabNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("ClosetabNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("ClosetabNotebook.label", {"side":
                                      "left", "sticky": ''}),
                                    ("ClosetabNotebook.close", {"side":
                                        "left", "sticky": ''}),]})]})]})])

        PNOTEBOOK = "ClosetabNotebook" 

        self.PNotebook1 = ttk.Notebook(self.master)
        self.PNotebook1.place(relx=0.049, rely=0.243, relheight=0.583
                , relwidth=0.906)
        self.PNotebook1.configure(width=734)
        self.PNotebook1.configure(takefocus="")
        self.PNotebook1.configure(style=PNOTEBOOK)
        #self.PNotebook1_t0 = tk.Frame(self.PNotebook1)
        #self.PNotebook1.add(self.PNotebook1_t0, padding=3)
        #self.PNotebook1.tab(0, text="Page 1",compound="none",underline="-1",)
        #self.PNotebook1_t0.configure(background="#d9d9d9")
        #self.PNotebook1_t0.configure(highlightbackground="#d9d9d9")
        #self.PNotebook1_t0.configure(highlightcolor="black")
        #self.PNotebook1_t1 = tk.Frame(self.PNotebook1)
        #self.PNotebook1.add(self.PNotebook1_t1, padding=3)
        #self.PNotebook1.tab(1, text="Page 2",compound="none",underline="-1",)
        #self.PNotebook1_t1.configure(background="#d9d9d9")
        #self.PNotebook1_t1.configure(highlightbackground="#d9d9d9")
        #self.PNotebook1_t1.configure(highlightcolor="black")
        self.PNotebook1.bind('<Button-1>',_button_press)
        self.PNotebook1.bind('<ButtonRelease-1>',_button_release)
        self.PNotebook1.bind('<Motion>',_mouse_over)


        self.tabs = {}
        self.Scrolledlistbox1 = {}
		#Ini udah bisa ngebuat tab loopnya, nanti nama roomnya tinggal dimasukan ke arraynya tab_names?
		#Tinggal buat scrolledlistboxnya... gimana caranya ngerubah self.Scrolledlistbox1 jadi self.Scrolledlistbox[i]? biar dia start dari 1 - banyaknya array.
		#Sama nanti pas insertnya tinggal disesuain sama nama roomnya.
        for tab_name in tab_names:
            tab = tk.Frame(self.PNotebook1)
            self.PNotebook1.add(tab, text=tab_name)
            self.tabs[tab_name] = tab
            self.tabs[tab_name].configure(background="#d9d9d9")
            self.tabs[tab_name].configure(highlightbackground="#d9d9d9")
            self.tabs[tab_name].configure(highlightcolor="black")
            self.Scrolledlistbox1[tab_name] = ScrolledListBox(self.tabs[tab_name])
            self.Scrolledlistbox1[tab_name].place(relx=0.0, rely=0.0, relheight=1.003
                    , relwidth=1.001)
            self.Scrolledlistbox1[tab_name].configure(background="white")
            self.Scrolledlistbox1[tab_name].configure(disabledforeground="#a3a3a3")
            self.Scrolledlistbox1[tab_name].configure(font="TkFixedFont")
            self.Scrolledlistbox1[tab_name].configure(foreground="black")
            self.Scrolledlistbox1[tab_name].configure(highlightbackground="#d9d9d9")
            self.Scrolledlistbox1[tab_name].configure(highlightcolor="#d9d9d9")
            self.Scrolledlistbox1[tab_name].configure(selectbackground="#c4c4c4")
            self.Scrolledlistbox1[tab_name].configure(selectforeground="black")
            self.Scrolledlistbox1[tab_name].configure(width=10)

        #message_list.append("halo")
        

        self.master.after(100, self.msgReceived)
        # for item in message_list:
        #     self.Scrolledlistbox1.insert(tk.END, item)

        self.Entry1 = tk.Entry(self.master, textvariable=my_msg)
        self.Entry1.place(relx=0.049, rely=0.851,height=30, relwidth=0.710)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(width=504)
        self.Entry1.bind("<Return>", self.send)

        self.Entry2 = tk.Entry(self.master)
        self.Entry2.place(relx=0.593, rely=0.035,height=30, relwidth=0.264)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")
        self.Entry2.configure(width=214)
        self.Entry2.insert(0,"Anonymous")
        self.Entry2.configure(justify='center')

        self.m_changenm = tk.Button(self.master, command=self.changeName)
        self.m_changenm.place(relx=0.87, rely=0.035, height=31, width=67)
        self.m_changenm.configure(activebackground="#ececec")
        self.m_changenm.configure(activeforeground="#000000")
        self.m_changenm.configure(background="#d9d9d9")
        self.m_changenm.configure(disabledforeground="#a3a3a3")
        self.m_changenm.configure(foreground="#000000")
        self.m_changenm.configure(highlightbackground="#d9d9d9")
        self.m_changenm.configure(highlightcolor="black")
        self.m_changenm.configure(pady="0")
        self.m_changenm.configure(text='''Change''')
        self.m_changenm.configure(width=57)

        self.ConnectedINFO = tk.LabelFrame(self.master)
        self.ConnectedINFO.place(relx=0.043, rely=0.017, relheight=0.217
                , relwidth=0.259)
        self.ConnectedINFO.configure(relief='groove')
        self.ConnectedINFO.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.ConnectedINFO.configure(foreground="#ffffff")
        self.ConnectedINFO.configure(text='''Connected On''')
        self.ConnectedINFO.configure(background="#31BA7F")
        self.ConnectedINFO.configure(width=210)

        self.m_hostname = tk.Label(self.ConnectedINFO)
        self.m_hostname.place(relx=0.024, rely=0.12, height=21, width=84
                , bordermode='ignore')
        self.m_hostname.configure(activebackground="#f9f9f9")
        self.m_hostname.configure(activeforeground="black")
        self.m_hostname.configure(background="#31BA7F")
        self.m_hostname.configure(disabledforeground="#a3a3a3")
        self.m_hostname.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.m_hostname.configure(foreground="#ffffff")
        self.m_hostname.configure(highlightbackground="#d9d9d9")
        self.m_hostname.configure(highlightcolor="black")
        self.m_hostname.configure(text='''Hostname :''')

        self.me_hostname = tk.Label(self.ConnectedINFO)
        self.me_hostname.place(relx=0.405, rely=0.12, height=21, width=109
                , bordermode='ignore')
        self.me_hostname.configure(background="#31BA7F")
        self.me_hostname.configure(disabledforeground="#a3a3a3")
        self.me_hostname.configure(foreground="#ffffff")
        self.me_hostname.configure(text=txtHost)
        self.me_hostname.configure(width=114)

        self.port_label_m = tk.LabelFrame(self.ConnectedINFO)
        self.port_label_m.place(relx=0.048, rely=0.32, relheight=0.6
                , relwidth=0.905, bordermode='ignore')
        self.port_label_m.configure(relief='groove')
        self.port_label_m.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.port_label_m.configure(foreground="#ffffff")
        self.port_label_m.configure(text='''Port''')
        self.port_label_m.configure(background="#31BA7F")
        self.port_label_m.configure(width=190)

        self.em_recv = tk.Label(self.port_label_m)
        self.em_recv.place(relx=0.368, rely=0.6, height=21, width=54
                , bordermode='ignore')
        self.em_recv.configure(activebackground="#f9f9f9")
        self.em_recv.configure(activeforeground="black")
        self.em_recv.configure(background="#31BA7F")
        self.em_recv.configure(disabledforeground="#a3a3a3")
        self.em_recv.configure(foreground="#ffffff")
        self.em_recv.configure(highlightbackground="#d9d9d9")
        self.em_recv.configure(highlightcolor="black")
        self.em_recv.configure(text=txtRecv)

        self.em_send = tk.Label(self.port_label_m)
        self.em_send.place(relx=0.684, rely=0.6, height=21, width=54
                , bordermode='ignore')
        self.em_send.configure(activebackground="#f9f9f9")
        self.em_send.configure(activeforeground="black")
        self.em_send.configure(background="#31BA7F")
        self.em_send.configure(disabledforeground="#a3a3a3")
        self.em_send.configure(foreground="#ffffff")
        self.em_send.configure(highlightbackground="#d9d9d9")
        self.em_send.configure(highlightcolor="black")
        self.em_send.configure(text=txtSend)

        self.m_ftp = tk.Label(self.ConnectedINFO)
        self.m_ftp.place(relx=0.095, rely=0.48, height=21, width=54
                , bordermode='ignore')
        self.m_ftp.configure(activebackground="#f9f9f9")
        self.m_ftp.configure(activeforeground="black")
        self.m_ftp.configure(background="#31BA7F")
        self.m_ftp.configure(disabledforeground="#a3a3a3")
        self.m_ftp.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.m_ftp.configure(foreground="#ffffff")
        self.m_ftp.configure(highlightbackground="#d9d9d9")
        self.m_ftp.configure(highlightcolor="black")
        self.m_ftp.configure(text='''FTP''')
        self.m_ftp.configure(width=54)

        self.m_recv = tk.Label(self.ConnectedINFO)
        self.m_recv.place(relx=0.357, rely=0.48, height=21, width=54
                , bordermode='ignore')
        self.m_recv.configure(activebackground="#f9f9f9")
        self.m_recv.configure(activeforeground="black")
        self.m_recv.configure(background="#31BA7F")
        self.m_recv.configure(disabledforeground="#a3a3a3")
        self.m_recv.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.m_recv.configure(foreground="#ffffff")
        self.m_recv.configure(highlightbackground="#d9d9d9")
        self.m_recv.configure(highlightcolor="black")
        self.m_recv.configure(text='''Recv''')
        self.m_recv.configure(width=54)

        self.m_send = tk.Label(self.ConnectedINFO)
        self.m_send.place(relx=0.643, rely=0.48, height=21, width=54
                , bordermode='ignore')
        self.m_send.configure(activebackground="#f9f9f9")
        self.m_send.configure(activeforeground="black")
        self.m_send.configure(background="#31BA7F")
        self.m_send.configure(disabledforeground="#a3a3a3")
        self.m_send.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.m_send.configure(foreground="#ffffff")
        self.m_send.configure(highlightbackground="#d9d9d9")
        self.m_send.configure(highlightcolor="black")
        self.m_send.configure(text='''Send''')
        self.m_send.configure(width=54)

        self.em_ftp = tk.Label(self.ConnectedINFO)
        self.em_ftp.place(relx=0.095, rely=0.68, height=21, width=54
                , bordermode='ignore')
        self.em_ftp.configure(activebackground="#f9f9f9")
        self.em_ftp.configure(activeforeground="black")
        self.em_ftp.configure(background="#31BA7F")
        self.em_ftp.configure(disabledforeground="#a3a3a3")
        self.em_ftp.configure(foreground="#ffffff")
        self.em_ftp.configure(highlightbackground="#d9d9d9")
        self.em_ftp.configure(highlightcolor="black")
        self.em_ftp.configure(text=txtFTP)
        self.em_ftp.configure(width=54)

        self.m_title = tk.Label(self.master)
        self.m_title.place(relx=0.531, rely=0.104, height=51, width=344)
        self.m_title.configure(background="#31BA7F")
        self.m_title.configure(disabledforeground="#a3a3a3")
        self.m_title.configure(font="-family {Segoe UI} -size 30 -weight bold")
        self.m_title.configure(foreground="#ffffff")
        self.m_title.configure(text='''Anonymous Chat''')
        self.m_title.configure(width=344)

        self.m_title2 = tk.Label(self.master)
        self.m_title2.place(relx=0.556, rely=0.191, height=21, width=324)
        self.m_title2.configure(background="#31BA7F")
        self.m_title2.configure(disabledforeground="#a3a3a3")
        self.m_title2.configure(font="-family {Segoe UI} -size 10 -weight bold")
        self.m_title2.configure(foreground="#ffffff")
        self.m_title2.configure(text='''Enjoy the sensation of chatting with your privacy''')
        self.m_title2.configure(width=324)

        self.m_emot = tk.Button(self.master, command=self.emoji_window)
        self.m_emot.place(relx=0.772, rely=0.851, height=30, width=35)
        self.m_emot.configure(activebackground="#ececec")
        self.m_emot.configure(activeforeground="#000000")
        self.m_emot.configure(background="#d9d9d9")
        self.m_emot.configure(disabledforeground="#a3a3a3")
        self.m_emot.configure(foreground="#000000")
        self.m_emot.configure(highlightbackground="#d9d9d9")
        self.m_emot.configure(highlightcolor="black")
        self.m_emot.configure(pady="0")
        self.m_emot.configure(text='''Emo''')
        self.m_emot.configure(width=37)

        self.e_addroom = tk.Entry(self.master)
        self.e_addroom.place(relx=0.049, rely=0.911,height=34, relwidth=0.249)
        self.e_addroom.configure(background="white")
        self.e_addroom.configure(disabledforeground="#a3a3a3")
        self.e_addroom.configure(font="TkFixedFont")
        self.e_addroom.configure(foreground="#000000")
        self.e_addroom.configure(insertbackground="black")
        self.e_addroom.configure(width=174)

        self.CreateRoom = tk.Button(self.master, command=self.createGroup)
        self.CreateRoom.place(relx=0.309, rely=0.913, height=34, width=145)
        self.CreateRoom.configure(activebackground="#ececec")
        self.CreateRoom.configure(activeforeground="#000000")
        self.CreateRoom.configure(background="#d9d9d9")
        self.CreateRoom.configure(disabledforeground="#a3a3a3")
        self.CreateRoom.configure(foreground="#000000")
        self.CreateRoom.configure(highlightbackground="#d9d9d9")
        self.CreateRoom.configure(highlightcolor="black")
        self.CreateRoom.configure(pady="0")
        self.CreateRoom.configure(text='''Add Room''')
        self.CreateRoom.configure(width=147)

        self.e_sendfile = tk.Entry(self.master,textvariable=path_msg)
        self.e_sendfile.place(relx=0.5, rely=0.911,height=34, relwidth=0.253)
        self.e_sendfile.configure(background="white")
        self.e_sendfile.configure(disabledforeground="#a3a3a3")
        self.e_sendfile.configure(font="TkFixedFont")
        self.e_sendfile.configure(foreground="#000000")
        self.e_sendfile.configure(highlightbackground="#d9d9d9")
        self.e_sendfile.configure(highlightcolor="black")
        self.e_sendfile.configure(insertbackground="black")
        self.e_sendfile.configure(selectbackground="#c4c4c4")
        self.e_sendfile.configure(selectforeground="black")
        self.e_sendfile.configure(state='readonly')
	
        self.b_browsefile = tk.Button(self.master, command=self.fileBrowse)
        self.b_browsefile.place(relx=0.760, rely=0.913, height=34, width=78)
        self.b_browsefile.configure(activebackground="#ececec")
        self.b_browsefile.configure(activeforeground="#000000")
        self.b_browsefile.configure(background="#d9d9d9")
        self.b_browsefile.configure(disabledforeground="#a3a3a3")
        self.b_browsefile.configure(foreground="#000000")
        self.b_browsefile.configure(highlightbackground="#d9d9d9")
        self.b_browsefile.configure(highlightcolor="black")
        self.b_browsefile.configure(pady="0")
        self.b_browsefile.configure(text='''Browse''')
		
        self.b_sendfile = tk.Button(self.master, command=self.sendFileFTP)
        self.b_sendfile.place(relx=0.860, rely=0.913, height=34, width=78)
        self.b_sendfile.configure(activebackground="#ececec")
        self.b_sendfile.configure(activeforeground="#000000")
        self.b_sendfile.configure(background="#d9d9d9")
        self.b_sendfile.configure(disabledforeground="#a3a3a3")
        self.b_sendfile.configure(foreground="#000000")
        self.b_sendfile.configure(highlightbackground="#d9d9d9")
        self.b_sendfile.configure(highlightcolor="black")
        self.b_sendfile.configure(pady="0")
        self.b_sendfile.configure(text='''Send File''')

        self.menubar = tk.Menu(self.master,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        self.master.configure(menu = self.menubar)

        self.m_sendmain = tk.Button(self.master, command=self.send)
        self.m_sendmain.place(relx=0.827, rely=0.851, height=29, width=104)
        self.m_sendmain.configure(activebackground="#ececec")
        self.m_sendmain.configure(activeforeground="#000000")
        self.m_sendmain.configure(background="#d9d9d9")
        self.m_sendmain.configure(disabledforeground="#a3a3a3")
        self.m_sendmain.configure(foreground="#000000")
        self.m_sendmain.configure(highlightbackground="#d9d9d9")
        self.m_sendmain.configure(highlightcolor="black")
        self.m_sendmain.configure(pady="0")
        self.m_sendmain.configure(text='''Send''')
        self.m_sendmain.configure(width=77)
        self.m_sendmain.bind("<Return>", self.send)
        self.recv = threading.Thread(target=self.inloop)
        self.recv.start()
        self.newResponse = ''
        global currentlyactivetab 
        currentlyactivetab = "public"
        self.msgReceived()
        self.UpdateTabs()

    def inloop(self):#<-----------------------Pesan Diterima di Ca.newREs => Cuma
        while True:
            if CA.resQueue.empty() == queue.Empty:
                continue
            self.newResponse = CA.resQueue.get()

            if self.newResponse.code == 211:
                receiving_message = self.newResponse.content["sender"] + "@" + self.newResponse.content["toGroup"]+": "+self.newResponse.content["message"]
                message_list.append(receiving_message)
                message_list_toGroup.append(self.newResponse.content["toGroup"])
            
            if self.newResponse.code == 310:
                receiving_message = "Server: " + self.newResponse.content["message"]
                message_list.append(receiving_message)
                message_list_toGroup.append("all")

            #elif self.newResponse.code == 410:
            #    message_list.append(self.newResponse.code)
            # print(message_list)

    def msgReceived(self):

        panjang = len(message_list) 
        for i in range(panjang):
            if message_list_toGroup[i] == "all":
                for key in self.Scrolledlistbox1:

                    rendermsg = rendertext(message_list[i])
                    self.Scrolledlistbox1[key].insert(tk.END, rendermsg)
            else:
                rendermsg = rendertext(message_list[i])
                self.Scrolledlistbox1[message_list_toGroup[i]].insert(tk.END, rendermsg)

        message_list[:] = []
        message_list_toGroup[:] = []
        self.master.after(100, self.msgReceived)

    def AddingGroupTab(self, tab_name):
        tab = tk.Frame(self.PNotebook1)
        tab_names.append(tab_name)
        self.PNotebook1.add(tab, text=tab_name)
        self.tabs[tab_name] = tab
        self.tabs[tab_name].configure(background="#d9d9d9")
        self.tabs[tab_name].configure(highlightbackground="#d9d9d9")
        self.tabs[tab_name].configure(highlightcolor="black")
        self.tabs[tab_name].bind()
        self.Scrolledlistbox1[tab_name] = ScrolledListBox(self.tabs[tab_name])
        self.Scrolledlistbox1[tab_name].place(relx=0.0, rely=0.0, relheight=1.003
                    , relwidth=1.001)
        self.Scrolledlistbox1[tab_name].configure(background="white")
        self.Scrolledlistbox1[tab_name].configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1[tab_name].configure(font="TkFixedFont")
        self.Scrolledlistbox1[tab_name].configure(foreground="black")
        self.Scrolledlistbox1[tab_name].configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1[tab_name].configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1[tab_name].configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1[tab_name].configure(selectforeground="black")
        self.Scrolledlistbox1[tab_name].configure(width=10)

    def UpdateTabs(self):

        maudidel = []

        for item in self.Scrolledlistbox1:
            if item in tab_names:
                continue
            else:
                maudidel.append(item)

        for item in maudidel:
            del self.Scrolledlistbox1[item]
            del self.tabs[item]
            CA.removeGroup(item)
        self.master.after(100, self.UpdateTabs)


    def send(self, event=None):  # event is passed by binders.
        """Handles sending of messages."""
        msg = self.Entry1.get()
        my_msg.set("")
        print (msg)
        # CA.sendMessage(msg)
        global currentlyactivetab
        CA.sendMessage(msg, currentlyactivetab)
        # message_list.append("You: " + msg)

    def changeName(self):
        CA.changeName(self.Entry2.get())

    def createGroup(self):
        CA.addGroup(self.e_addroom.get())
        self.AddingGroupTab(self.e_addroom.get())

    def sendFileFTP(self):
        global currentlyactivetab
        if self.e_sendfile.get() != "":
            CA.sendFile(self.e_sendfile.get(), self.Entry1.get(), currentlyactivetab)

    def fileBrowse(self):
        print('now')
        p = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("Image files","*.jpg;*.png;*.gif"),("Document files","*.pdf;*.doc,;*.docx"),("all files", "*.*")))
        print(os.path.isfile(p))
        path_msg.set(p)
        print(p)

    def emoji_window(self):
        t = tk.Toplevel(self.master)
        emojiFrame = tk.Frame(t)
        t.resizable(False, False)
        listbutton = []
        for coll in range(5):
            for roww in range ((int(len(emo.label)/5))):
                button = {}
                # button['val'] = rendertext(emo.label[coll*(roww-1)+roww])
                button['val'] = rendertext(emo.label[roww*4+coll])
                button['text'] = emo.label[roww*4+coll]
                button['widget'] = tk.Button(emojiFrame,fg="black",text=rendertext(button['val']),command=partial(self.addtosend,button['text']))
                button['widget'].config(font=("Courier", 25))
                button['widget'].grid(row=roww,column=coll)
                listbutton.append(button)
        emojiFrame.pack(expand=True,fill="both")

    def addtosend(self,val):
        my_msg.set(my_msg.get()+val)

# The following code is add to handle mouse events with the close icons
# in PNotebooks widgets.
def _button_press(event):
    widget = event.widget
    element = widget.identify(event.x, event.y)
    if "close" in element:
        index = widget.index("@%d,%d" % (event.x, event.y))
        widget.state(['pressed'])
        widget._active = index
        print(event.widget.tab(index, "text"))
    else:
        index = widget.index("@%d,%d" % (event.x, event.y))
        terpilih = event.widget.tab(index, "text")
        global currentlyactivetab
        currentlyactivetab = terpilih

def _button_release(event):
    widget = event.widget
    if not widget.instate(['pressed']):
            return
    element = widget.identify(event.x, event.y)
    try:
        index = widget.index("@%d,%d" % (event.x, event.y))
    except TclError:
        pass
    if "close" in element and widget._active == index:
        closed = event.widget.tab(index, "text")
        tab_names.remove(closed)
        print(tab_names)
        widget.forget(index)
        widget.event_generate("<<NotebookTabClosed>>")

    widget.state(['!pressed'])
    widget._active = None

def _mouse_over(event):
    widget = event.widget
    element = widget.identify(event.x, event.y)
    if "close" in element:
        widget.state(['alternate'])
    else:
        widget.state(['!alternate'])

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

def main():
    root=tk.Tk()
    myGUIWelcome=Welcome(root)
    # myGUIWelcome=AnonWinMain(root)

    root.mainloop()

if __name__ == '__main__':
    main()
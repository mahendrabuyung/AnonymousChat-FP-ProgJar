import sys

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

import v_username_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Box___Take_a_Username (root)
    v_username_support.init(root, top)
    root.mainloop()

w = None
def create_Box___Take_a_Username(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Box___Take_a_Username (w)
    v_username_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Box___Take_a_Username():
    global w
    w.destroy()
    w = None

class Box___Take_a_Username:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("352x182+443+159")
        top.title("Anonymous Chat")
        top.configure(background="#00ff00")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.FrameBox = tk.Frame(top)
        self.FrameBox.place(relx=0.028, rely=0.082, relheight=0.852
                , relwidth=0.923)
        self.FrameBox.configure(relief='groove')
        self.FrameBox.configure(borderwidth="2")
        self.FrameBox.configure(relief="groove")
        self.FrameBox.configure(background="#00ff00")
        self.FrameBox.configure(highlightbackground="#d9d9d9")
        self.FrameBox.configure(highlightcolor="black")
        self.FrameBox.configure(width=325)

        self.Take_a_Username = tk.LabelFrame(self.FrameBox)
        self.Take_a_Username.place(relx=0.046, rely=0.097, relheight=0.613
                , relwidth=0.892)
        self.Take_a_Username.configure(relief='groove')
        self.Take_a_Username.configure(foreground="black")
        self.Take_a_Username.configure(text='''Take a Username:''')
        self.Take_a_Username.configure(background="#00ff00")
        self.Take_a_Username.configure(highlightbackground="#d9d9d9")
        self.Take_a_Username.configure(highlightcolor="black")
        self.Take_a_Username.configure(width=290)

        self.Entry1 = tk.Entry(self.Take_a_Username)
        self.Entry1.place(relx=0.052, rely=0.368, height=33, relwidth=0.879
                , bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(justify='center')
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Lets_Chat = tk.Button(self.FrameBox)
        self.Lets_Chat.place(relx=0.508, rely=0.774, height=24, width=68)
        self.Lets_Chat.configure(activebackground="#ececec")
        self.Lets_Chat.configure(activeforeground="#000000")
        self.Lets_Chat.configure(background="#d9d9d9")
        self.Lets_Chat.configure(disabledforeground="#a3a3a3")
        self.Lets_Chat.configure(foreground="#000000")
        self.Lets_Chat.configure(highlightbackground="#d9d9d9")
        self.Lets_Chat.configure(highlightcolor="black")
        self.Lets_Chat.configure(pady="0")
        self.Lets_Chat.configure(text='''Let's Chat''')

        self.Kembali = tk.Button(self.FrameBox)
        self.Kembali.place(relx=0.738, rely=0.774, height=24, width=62)
        self.Kembali.configure(activebackground="#ececec")
        self.Kembali.configure(activeforeground="#000000")
        self.Kembali.configure(background="#d9d9d9")
        self.Kembali.configure(disabledforeground="#a3a3a3")
        self.Kembali.configure(foreground="#000000")
        self.Kembali.configure(highlightbackground="#d9d9d9")
        self.Kembali.configure(highlightcolor="black")
        self.Kembali.configure(pady="0")
        self.Kembali.configure(text='''Kembali''')

if __name__ == '__main__':
    vp_start_gui()





